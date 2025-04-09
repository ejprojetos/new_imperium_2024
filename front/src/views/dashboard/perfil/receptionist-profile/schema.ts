import { receptionistSchema } from '@/lib/schema'
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'

const schema = receptionistSchema

export const receptionistDataSchema: ReturnType<typeof toTypedSchema> = toTypedSchema(schema)
export type ReceptionistDataSchema = z.infer<typeof schema>
