import { fetcher } from './fetcher.service'
import type { User } from '@/types/users.types'

export const userService = {
    getDoctors: () => fetcher<User[]>('/users/users_doctors')
}
