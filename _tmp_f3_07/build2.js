const fs=require('fs');
const base='D:/librebsd/';
const outPath=base+'script/_db_row_mining/audit_outline/judgements/f3_07_s078.jsonl';
const shard=fs.readFileSync(base+'script/_db_row_mining/audit_outline/shards/f3_07_s078.jsonl','utf8').replace(/^/, '').split('\n').filter(x=>x.trim()).map(JSON.parse);
const tail='以上为邮件列表当事人一手自述，属过程性证据，不得单独引为定论。';
const cn=s=>(s.match(/[一-鿿]/g)||[]).length;

const raw=fs.readFileSync(base+'_tmp_f3_07/cn.txt','utf8').replace(/^/, '');
let rows=[],cur=null,buf='';
for(const line of raw.split('\n')){
  if(line.startsWith('@@')){ if(cur!==null){rows.push(buf);} cur=parseInt(line.slice(2),10); buf=''; continue; }
  if(cur===null) continue;
  if(line.startsWith('正文：')){ buf+=line.slice(3); continue; }
  buf+=line;
}
if(cur!==null) rows.push(buf);

const ev=require(base+'_tmp_f3_07/ev.js');
const reasons=[
'src_body 中 Gibbs 自述 Individual developers are allowed to commit to the central repository for FreeBSD, but not in Linux 以及 Scott 的变更日志取自公司 Perforce 仓库、近期 FreeBSD 仓库由 Scott 代管，正文忠实；仅原摘要缺纪律串收尾且正文 107 汉字远超 80 上限',
'src_body 补丁头部 Convert FALSE to false 与 diff 中 __FreeBSD__ 下 Don not mark the user request 及 CAM_BDR_SENT 参数均在原文；正文 79 汉字合规，仅原摘要以代码片段收尾、缺纪律串',
'src_body 中 please don\'t hard-code qlogic in the license 与唯一愿意双许可的是 openbsd 极简 mit-style 许可证、许可证模板链接均在原文，贡献文件清单则为 I\'ll also send you a list 的后续承诺；原摘要 117 汉字超上限且把承诺写成已附，须按源文改写',
'src_body 中 FreeBSD 驱动有 896 rev 1 workaround 的结论出自被 Hellwig 引用的 Makisara 原话，原摘要以 Makisara 说明 表述准确；正文 64 汉字合规，仅缺纪律串收尾',
'src_body 仅为 2003 年 10 月一份快照，未提供跨期延续证据，原摘要 长期 属源文无据的时长断言，须删除；原正文 95 汉字亦超 80 上限',
'src_body 中 Strand 补充 aic79xx 与 39320A-R 在旧内核上出现问题、改用 39160 后 aic7xx 驱动能自行恢复、并引用他人建议检查线缆端接与 OpenBSD 旧帖，与正文相符；正文 53 汉字合规，仅缺纪律串收尾',
'src_body 中 Could not release a substantial majority of it because it would violate licensed libraries 与开源社区在 BSD 许可证下未提交任何改动均与正文相符；正文 85 汉字超 80 上限',
'src_body 中 Andersen 称不知 bksend 压缩包为何物、file 结果显示 ASCII English text、并询问是否有 unified diff 或 tarball，与正文相符；正文 74 汉字合规，仅缺纪律串收尾',
'src_body 补丁新增行中注释 netbsd turns off ints here, why not be safe and do it too 紧随其后即 local_irq_save(flags) 与 sun3scsi_dma_start 发送链，与正文相符；正文 73 汉字合规，仅缺纪律串收尾',
'src_body 中 Leech 回应 Hellwig 的 lib 建议并说明 Rob 建立开放仓库前已把多数 TAILQ 宏转为 list_head、仅 sa_event 一处遗留并希望改用通知链，与正文相符；正文 104 汉字超上限',
'src_body 中 Garzik 称 excessive interrupts 问题由 Jon Burgess 追踪到 ICH5 硬件问题、附 FreeBSD 存档帖链接并提交补丁、自己打算改写得更聚焦 ata_piix，与正文相符；正文 66 汉字合规，仅缺纪律串收尾',
'src_body 只给出 Adaptec 管理工具一例，原摘要 反映出 BSD 许可证本身未必能激活社区协作 超出单一例证得出的普遍结论，已收窄；正文 69 汉字合规，仅缺纪律串收尾',
'src_body 中 FreeBSD 未出现数据损坏的说法出自被 Sonnenburg 引用的 Tejun Heo 那段，其中还夹着 Jeff Garzik 关于 PCI FIFO 复制的自述，并非 Sonnenburg 本人所引；原摘要把它归到 Sonnenburg 名下属归属倒挂，须按源文改写',
'src_body 中 Carpani 称使用 Justin 在 people.freebsd.org 的驱动（ver 2.0.12）、主线内核自带的版本对他太不稳定、内核常在初始化 SCSI 子系统时挂起，与正文相符；正文 39 汉字合规，仅缺纪律串收尾',
'src_body 中 Jeff Garzik 引述 Andree 的话称他曾询问能否参考 FreeBSD 的 ataraid(4) 驱动来学习 Intel ICHx-R SoftRAID 格式、FreeBSD 能识别而 dmraid 不行，与正文相符；原正文仅 29 汉字低于 30 下限，已补足',
'src_body 中 Gibb 自述内核版本、1.3.10、未采用 Justin 源文件因其只宣称适配 2.4.20，Beutin 关于 SRC 目录的询问另起一句并由 Gibb 转述，归属标注正确；原正文 126 汉字超上限',
'src_body 中 Mansfield 转述 Gibbs 的话给出 linux-2.5-aic79xxx.tar.gz 链接并说明该更新同时尊重有序标签机制，正文标注该链接出自 Gibbs 早前发言，归属正确；正文 38 汉字合规，仅缺纪律串收尾',
'src_body 中 Bottomley 的 pull 说明明确列出 Alex Dewar (1): scsi: aic7xxx: Remove more FreeBSD-specific code，与正文相符；正文 32 汉字合规，仅缺纪律串收尾',
'src_body 补丁说明第二点 Remove the BSD dual licence on the new work 与第一点 Cleanup, linuxise, demacro 均在原文，正文忠实；正文 38 汉字合规，仅缺纪律串收尾',
'src_body 中 Gilbert 逐条说明 Linux 侧自 2.4 中段起无已知问题、原发帖人过早下结论、Gibbs 告知并无此问题、最终帖的 READ(10) 失败追踪与 32 位 LBA 默认读法指向端接问题，与正文相符；原正文 122 汉字超上限',
'src_body 中 Hedrick 先写自己评论 Would have been nice to list such rules at the top if the MAINTAINERS file，随后引用 Linus 对 Gibbs 提问的完整回复，归属与顺序均与原文一致；正文 52 汉字合规，但原摘要使用被禁的中文直角引号并把原文长引文整段直引，须改写为间接表述',
'src_body 中 Petersen 引述 Dewar 的话称 FreeBSD 专属代码自 cca6cb8ad7a8 起已无必要，并回复已合入 5.7/scsi-queue，与正文相符；原正文仅 28 汉字低于 30 下限，已补足',
'src_body 中 Berthiaume 自述 2.4.19 与 reiserfs 上的测试条件、启用写缓存带来大幅性能改善、叠加写屏障补丁仅轻微下降、无法就 SCSI 发言；线程底部 Jordan Breeding 提问 FreeBSD CAM 层实现、Bottomley 回答 Actually no，归属均正确；原正文 127 汉字超上限'
];
const issues=[
['正文 107 汉字超 80 上限','缺纪律串收尾','原以英文引语结尾且其后接中文句号，标点不成对'],
['缺纪律串收尾','原以 #ifdef __FreeBSD__ 代码片段收尾而非纪律串'],
['正文 117 汉字超 80 上限','原把 将另补发贡献文件清单 写成已附，属时态失实','缺纪律串收尾'],
['缺纪律串收尾'],
['正文 95 汉字超 80 上限','原称上游 长期 部署于 BSD 站点属源文无据的时长断言，已删','缺纪律串收尾'],
['缺纪律串收尾'],
['正文 85 汉字超 80 上限','缺纪律串收尾'],
['缺纪律串收尾'],
['缺纪律串收尾'],
['正文 104 汉字超 80 上限','缺纪律串收尾'],
['缺纪律串收尾'],
['原称 BSD 许可证未必能激活社区协作，超出单一例证得出的普遍结论，已收窄','缺纪律串收尾'],
['归属倒挂：把 Tejun Heo 转述的 FreeBSD 无数据损坏结论误归给 Soeren Sonnenburg','正文须按源文重写','缺纪律串收尾'],
['缺纪律串收尾'],
['原文正文仅 29 汉字低于 30 下限，已补足','缺纪律串收尾'],
['正文 126 汉字超 80 上限','缺纪律串收尾'],
['缺纪律串收尾'],
['缺纪律串收尾'],
['缺纪律串收尾'],
['正文 122 汉字超 80 上限','缺纪律串收尾'],
['原使用被禁的中文直角引号包英文长引文，已改为间接表述','原 著名回复 与 关键文本 属评判性表述，已中性化','缺纪律串收尾'],
['原文正文仅 28 汉字低于 30 下限，已补足','缺纪律串收尾'],
['正文 127 汉字超 80 上限','原含 该封邮件未提及 FreeBSD CAM 层 一类对源文缺述的说明，已删','缺纪律串收尾']
];
const verdicts=[
'fix-format','fix-format','fix-text','fix-format','fix-text','fix-format','fix-format','fix-format','fix-format','fix-format',
'fix-format','fix-text','fix-text','fix-format','fix-format','fix-format','fix-format','fix-format','fix-format','fix-format',
'fix-format','fix-format','fix-format'
];

if(rows.length!==23||ev.length!==23||reasons.length!==23||issues.length!==23||verdicts.length!==23||shard.length!==23){
  throw new Error('length mismatch rows='+rows.length+' ev='+ev.length+' shard='+shard.length);
}
let errs=0;
rows.forEach((b,i)=>{
  const c=cn(b);
  if(c<30||c>80){console.log('L'+(i+1)+' CN='+c+' OUT');errs++;}
  if(/[「」『』*]/.test(b)){console.log('L'+(i+1)+' BANNED');errs++;}
  if(/["“”]/.test(b)){console.log('L'+(i+1)+' QUOTE');errs++;}
  if(ev[i].length>200){console.log('L'+(i+1)+' EV='+ev[i].length);errs++;}
  console.log('L'+(i+1)+' CN='+c+' EV='+ev[i].length+' '+verdicts[i]);
});
if(errs){throw new Error('precheck failed: '+errs);}

const lines=shard.map((s,i)=>JSON.stringify({key:s.key,'判定':verdicts[i],'新摘要句':rows[i]+tail,'理由':reasons[i],'证据':ev[i],'问题':issues[i]}));
const text=lines.join('\n')+'\n';
fs.writeFileSync(outPath,text,'utf8');
const back=fs.readFileSync(outPath);
console.log('BOM='+(back[0]===0xEF)+' CR='+text.includes('\r'));
const chk=text.split('\n').filter(x=>x.trim());
let tall={};
chk.forEach((l,i)=>{const o=JSON.parse(l);if(o.key!==shard[i].key)throw new Error('key mismatch L'+(i+1));tall[o['判定']]=(tall[o['判定']]||0)+1;});
console.log('LINES='+chk.length+' TALLY='+JSON.stringify(tall));
