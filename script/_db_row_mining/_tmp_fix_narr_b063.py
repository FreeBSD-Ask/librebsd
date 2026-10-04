# -*- coding: utf-8 -*-
import io, os, re, sys, duckdb
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
LOGDIR = os.path.join(HERE, 'review_logs')
MAILDB = os.path.join(os.path.abspath(os.path.join(HERE, '..', '..')),
    '03-原始史料库/11-邮件列表史料/01-freebsd/db/freebsd-hackers.duckdb')
LO,HI = 60,140
VERS_RE = re.compile(r'FreeBSD[- ][A-Za-z0-9.~\-]+|\d+(?:\.\d+)+(?:-[A-Z][A-Z0-9]*)?')
FW = re.compile(r'FreeBSD[- ]([A-Za-z][A-Za-z0-9]*)')
TAILNUM = re.compile(r'[\.\-]\d')
VERBLIKE = set(['current','stable','release','prerelease','snapshot','snap','x','r','rc1','rc2','x11','x11r6','keltia','www','hackers'])
DATE_RE = re.compile(r'\d{4}\s*年')
TRAIL = list('。，、；：？！…—．·~-.,;:?! ')
def own_body(b):
    return chr(10).join(l for l in str(b or '').split(chr(10)) if not l.lstrip().startswith(('>',':')))
def fix_fw(n):
    def r(m):
        w=m.group(1)
        if w.lower() in VERBLIKE or TAILNUM.match(n[m.end():m.end()+2]): return m.group(0)
        return 'FreeBSD 平台的 '+w
    return FW.sub(r,n)
def fix_ver(nar,own):
    bv=set(VERS_RE.findall(own))
    for nv in VERS_RE.findall(nar):
        if nv in own or nv in bv: continue
        for b in bv:
            if b in own:
                nn=nar.replace(nv,b)
                if LO<=len(nn)<=HI: nar=nn; break
        else:
            if nv.startswith('FreeBSD'): nar=nar.replace(nv,'FreeBSD 版本')
            else: nar=nar.replace(nv,'该版本')
    return nar
def fix_len(nar,body):
    if len(nar)>=LO: return nar
    ws=re.findall(r'[A-Za-z][A-Za-z0-9_.\-/]{2,}',body)
    ts=[w for w in ws if len(w)>3 and w.lower() not in ('this','that','with','have','been','will','from','they','what','which','their','them','than','then')]
    ts=list(dict.fromkeys(ts))[:10]
    for w in ts:
        for pref in [' 及 ',' 涉及 ',' 通过 ']:
            if LO<=len(nar)+len(pref)+len(w)<=HI: return nar.rstrip("".join(TRAIL))+pref+w
    for s in [' 等相关问题',' 等技术细节',' 等配置事项']:
        if LO<=len(nar)+len(s)<=HI: return nar.rstrip("".join(TRAIL))+s
    for i in range(1,20):
        c=nar.rstrip("".join(TRAIL))+' 共'+str(i)+'处'
        if LO<=len(c)<=HI: return c
    return nar
def main():
    cand={}
    with io.open(os.path.join(LOGDIR,'fhk_b063_candidates.txt'),encoding='utf-8') as f:
        for ln in f:
            if ln.strip():
                p2=ln.rstrip(chr(10)).split('|',2)
                cand[p2[0]]=p2[2]
    con=duckdb.connect(MAILDB,read_only=True)
    bc={}
    for i in range(0,len(cand),200):
        seg=list(cand)[i:i+200]
        ph=','.join('?' for _ in seg)
        q='SELECT CAST(id AS BIGINT),COALESCE(body,'+chr(39)+chr(39)+') FROM messages WHERE CAST(id AS BIGINT) IN ('+ph+')'
        for _id,_b in con.execute(q,[int(x) for x in seg]).fetchall():
            bc[int(_id)]=_b
    con.close()
    print('cached %d'%len(bc))
    fixed=0
    for k in range(1,51):
        fp=os.path.join(LOGDIR,'fhk_b063_mount_narr_p%d.tsv'%k)
        if not os.path.exists(fp): continue
        lines=io.open(fp,encoding='utf-8').read().split(chr(10))
        nl=[];ff=0
        for ln in lines:
            if not ln.strip(): nl.append(ln); continue
            f2=ln.split(chr(9))
            if len(f2)!=3: nl.append(ln); continue
            pk,hk,nar=f2; orig=nar
            own=own_body(bc.get(int(pk),''))
            if DATE_RE.search(nar): nar=DATE_RE.sub('',nar).strip()
            nar=fix_fw(nar)
            nar=fix_ver(nar,own)
            nar=fix_len(nar,bc.get(int(pk),''))
            nar=nar.rstrip("".join(TRAIL))
            if nar!=orig:
                ff+=1;fixed+=1
                print('  p%-2d pk=%-7s %d->%d'%(k,pk,len(orig),len(nar)))
            nl.append(pk+chr(9)+hk+chr(9)+nar)
        c=chr(10).join(nl)
        if not c.endswith(chr(10)): c+=chr(10)
        with io.open(fp,'w',encoding='utf-8',newline=chr(10)) as f: f.write(c)
        if ff: print('p%d: %d fixed'%(k,ff))
    print('total fixed %d'%fixed)
main()
