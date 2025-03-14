<script setup lang="ts">
import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
    AlertDialogTrigger
} from '@/components/ui/alert-dialog'
import { Button } from '@/components/ui/button'
import { useRouter, useRoute } from 'vue-router'
import { useMutation } from '@tanstack/vue-query'
import { fetcher } from '@/services/fetcher.service'
import { useToast } from '@/components/ui/toast/use-toast'

const { toast } = useToast()
const route = useRoute()
const router = useRouter()
const receptionistId = route.params.id as string

const { isPending, mutate } = useMutation({
    mutationFn: async () =>
        await fetcher(`/users/${receptionistId}/`, {
            method: 'DELETE'
        }),
    onSuccess: () => {
        toast({
            variant: 'success',
            description: 'Recepcionista removido com sucesso!'
        })
        router.push('/dashboard/recepcionistas')
    },
    onError: () => {
        toast({
            variant: 'destructive',
            description: 'Erro ao remover recepcionista! 😢'
        })
    }
})

function handleDelete() {
    mutate()
}
</script>

<template>
    <AlertDialog>
        <AlertDialogTrigger as-child>
            <Button variant="destructive">Deletar</Button>
        </AlertDialogTrigger>
        <AlertDialogContent>
            <AlertDialogHeader>
                <AlertDialogTitle>Você tem certeza que deseja remover?</AlertDialogTitle>
                <AlertDialogDescription>
                    Esta ação não pode ser desfeita. Isso excluirá permanentemente o recepcionista e
                    removerá seus dados de nossos servidores.
                </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogCancel>Cancelar</AlertDialogCancel>
                <AlertDialogAction @click="handleDelete">
                    <Loader v-if="isPending" class="animate-spin size-4" />
                    Deletar
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>
</template>
