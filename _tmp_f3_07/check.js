const fs=require('fs');
const p='D:/librebsd/_tmp_f3_07/drafts.txt';
const raw=fs.readFileSync(p,'utf8').replace(/^/, '');
const cn=s=>(s.match(/[一-鿿]/g)||[]).length;
let rows=[],cur=null,buf='';
for(const line of raw.split('\n')){
  if(line.startsWith('@@')){ if(cur){rows.push({n:cur,body:buf});} cur=parseInt(line.slice(2),10); buf=''; continue; }
  if(cur===null) continue;
  if(line.startsWith('正文：')){ buf+=line.slice(3); continue; }
  buf+=line;
}
if(cur){rows.push({n:cur,body:buf});}
let bad=0;
rows.forEach(r=>{
  const c=cn(r.body);
  const flag = (c<30||c>80)?'OUT':'ok';
  if(c<30||c>80) bad++;
  const banned=[...'「」『』*'].some(x=>r.body.includes(x));
  console.log('L'+r.n+' CN='+c+' '+flag+(banned?' BANNED':'')+' totalChars='+r.body.length);
});
console.log('rows='+rows.length+' bad='+bad);
