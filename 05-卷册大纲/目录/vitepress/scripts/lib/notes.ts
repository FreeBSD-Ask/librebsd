/**
 * 溯源注分类与锚点构造（站点侧复刻装配页判据）。
 *
 * 分类判据源＝`05-卷册大纲/目录/assets/doc.js` 块 3“1. 注三色分类”：
 *   ①命中 /(迁入|并入|拆分迁入|移入|原第)/ → 迁移（k-mig，teal）
 *   ②否则命中 /(分工|正身|互注|交叉引用|本节载|彼处载)/ → 分工（k-xref，accent）
 *   ③余下 → 史料（k-src，gold）
 * 装配页在运行时对 `.src` 文本做该判定；站点改在构建期判定并写入 class，
 * 省掉一次全量 DOM 扫描，图例计数也随之确定（同一判据、同一优先级序）。
 */

export type NoteKind = "xref" | "mig" | "src";

const MIG = /(迁入|并入|拆分迁入|移入|原第)/;
const XREF = /(分工|正身|互注|交叉引用|本节载|彼处载)/;

export function classifyNote(text: string): NoteKind {
  if (MIG.test(text)) return "mig";
  if (XREF.test(text)) return "xref";
  return "src";
}

export const NOTE_CLASS: Record<NoteKind, string> = {
  xref: "note-x k-xref",
  mig: "note-x k-mig",
  src: "note-x k-src",
};

/** 注组串（同一节的多个 〔…〕 以空格相连，与装配页 .src 文本一致）。 */
export function noteKind(groups: string[]): NoteKind {
  return classifyNote(groups.join(" "));
}

/** HTML 文本节点转义：注以整行 HTML 块写盘（markdown-it 不再解析其内联语法），故只需转义实体字符。 */
export function htmlEsc(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

/**
 * 装配页式锚点（C6 统一）：
 *   卷 vol-N ／ 章 vol-N-ch-M ／ 节 vol-N-ch-M-sec-A-B ／ 小节 …-sec-A-B-sub-K
 * K 为节内序号（1 起），与装配页 `id="vol-1-ch-1-sec-1-1-sub-1"` 同式。
 */
export const volAnchor = (v: number) => `vol-${v}`;
export const chAnchor = (v: number, c: number) => `vol-${v}-ch-${c}`;
export const secAnchor = (v: number, c: number, num: string) =>
  `vol-${v}-ch-${c}-sec-${num.replace(/\./g, "-")}`;
export const subAnchor = (v: number, c: number, secNum: string, k: number) =>
  `${secAnchor(v, c, secNum)}-sub-${k}`;

/** 小节页路由段：`1.1.1` → `1-1-1`（站点路由 `vNN/cMM/1-1-1`，2026-11-22 立）。 */
export const subSlug = (num: string) => num.replace(/\./g, "-");
export const subPath = (v: number, c: number, num: string, base = "") => {
  const p2 = (n: number) => String(n).padStart(2, "0");
  return `${base}/v${p2(v)}/c${p2(c)}/${subSlug(num)}`;
};
