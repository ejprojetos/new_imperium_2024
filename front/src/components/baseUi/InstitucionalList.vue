<template>
    <div class="space-y-6">
        <div class="overflow-hidden bg-white shadow-lg rounded-3xl">
            <div class="p-4 text-white bg-primary">
                <h2 class="text-lg font-semibold">Institucional</h2>
            </div>
            <ul>
                <li v-for="page in pages" :key="page.id" class="border-b last:border-b-0">
                    <div class="flex items-center justify-between p-4 hover:bg-blue-200">
                        <div class="flex-grow">
                            <span class="font-semibold">{{ page.name }}</span>
                        </div>
                        <button
                            @click="openPage(page.path)"
                            class="px-4 py-2 text-white transition-colors bg-blue-600 rounded-md hover:bg-blue-800">
                            Editar
                        </button>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

interface Pages {
    id: number
    name: string
    path: string
}

const pages = ref<Pages[]>([
    {
        id: 1,
        name: 'Seção Inicial',
        path: '/dashboard/institucional/secao-inicial'
    },
    {
        id: 2,
        name: 'Fluxo de Trabalho',
        path: '/dashboard/institucional/fluxo'
    },
    {
        id: 3,
        name: 'Features',
        path: '/dashboard/institucional/features'
    },
    {
        id: 4,
        name: 'Depoimentos',
        path: '/dashboard/institucional/depoimentos'
    }
])

const openPage = (path: string) => {
    router.push(path)
}
</script>

<style scoped>
ul {
    list-style: none;
    padding: 0;
}

ul li:nth-child(even) {
    background-color: #deecfa;
}
</style>
