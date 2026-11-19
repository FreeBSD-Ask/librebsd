/**
 * 构建期数据加载：DATA 段（catalog.json 的 persons／refs／revs 三视图）。
 * 消费方：theme/components/DataPanel.vue（首页数据视图）。只在首页加载。
 */
import { defineLoader } from 'vitepress'
import { CATALOG_JSON_PATH, readCatalogJson } from '../scripts/lib/source'

export interface PersonD {
  id: string; zh: string; en: string[]; role: string; priority: string; volume: string; life: string
}
export interface RevD { id: string; date: string; desc: string; status: string }
export interface DataSegment {
  persons: PersonD[]
  refs: Array<[string, string]>
  revs: RevD[]
}

declare const data: DataSegment
export { data }

type RawPerson = {
  id?: string
  names?: { zh?: string[]; en?: string[] }
  role?: string
  priority?: string
  volume?: string
  status?: { alive?: boolean; birth?: string | null; death?: string | null; note?: string }
}

export default defineLoader({
  watch: [CATALOG_JSON_PATH],
  load(): DataSegment {
    const raw = readCatalogJson()
    const persons: PersonD[] = (raw.persons as RawPerson[]).map((p) => {
      const b = p.status?.birth ?? ''
      const d = p.status?.death ?? ''
      const life = b || d ? `${b}${b && d ? '—' : ''}${d}` : p.status?.alive ? '在世' : ''
      return {
        id: p.id ?? '',
        zh: p.names?.zh?.[0] ?? '',
        en: p.names?.en ?? [],
        role: p.role ?? '',
        priority: p.priority ?? '',
        volume: p.volume ?? '',
        life,
      }
    })
    const refs = Object.entries(raw.refs).sort((a, b) => Number(a[0]) - Number(b[0])) as Array<[string, string]>
    const revs: RevD[] = (raw.revs as unknown[][]).map((r) => ({
      id: String(r[0] ?? ''), date: String(r[1] ?? ''), desc: String(r[2] ?? ''), status: String(r[3] ?? ''),
    }))
    return { persons, refs, revs }
  },
})
