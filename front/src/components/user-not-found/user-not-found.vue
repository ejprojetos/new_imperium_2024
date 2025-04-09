<script setup lang="ts">
import { defineProps } from 'vue'
import { RouterLink } from 'vue-router'

import { Button } from '@/components/ui/button'

defineProps<{
    navigateTo: string
}>()
</script>

<template>
    <div class="flex justify-center items-center h-full flex-col">
        <img src="../../assets/pacientes404.svg" alt="Médicos" class="w-64" />
        <h2 class="text-2xl font-medium mt-4">Usuário não encontrado!</h2>
        <p class="text-zinc-500 max-w-md text-center text-sm">
            Desculpe, nós não encontramos esse usuário, verifique se esse usuário existe ou tente
            mais tarde
        </p>

        <Button class="mt-4" asChild>
            <RouterLink :to="navigateTo">Voltar</RouterLink>
        </Button>
    </div>
</template>
