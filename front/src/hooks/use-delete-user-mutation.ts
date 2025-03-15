import { fetcher } from '@/services/fetcher.service'
import { useMutation } from '@tanstack/vue-query'

export function useDeleteUserMutation() {
    const result = useMutation({
        mutationFn: async (userId: string) =>
            await fetcher(`/users/${userId}/`, {
                method: 'DELETE'
            })
    })

    return result
}
