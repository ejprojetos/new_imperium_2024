<template>
    <LayoutDashboard>
        <div class="container mx-auto px-4 py-8">
            <h1 class="text-2xl font-bold text-center text-blue-900 mb-12">Suporte ao usuário</h1>

            <div class="max-w-4xl mx-auto">
                <!-- Resources Section -->
                <div class="bg-white rounded-lg shadow-md p-6 mb-8 grid grid-cols-2 gap-8">
                    <RouterLink
                        to="/dashboard/suporte/manual-usuario"
                        class="flex flex-col items-center hover:opacity-80 transition-opacity">
                        <img :src="manualIcon" alt="Manual" class="w-16 h-16 mb-2" />
                        <span class="text-blue-900">Manual do usuário</span>
                    </RouterLink>

                    <RouterLink
                        to="/dashboard/suporte/documentos"
                        class="flex flex-col items-center hover:opacity-80 transition-opacity">
                        <img :src="documentIcon" alt="Documentos" class="w-16 h-16 mb-2" />
                        <span class="text-blue-900">Outros documentos</span>
                    </RouterLink>
                </div>

                <!-- FAQ Section -->
                <div class="mt-8">
                    <h2 class="text-xl font-bold text-blue-900 mb-6">Dúvidas frequentes</h2>

                    <div class="space-y-4">
                        <div
                            v-for="(faq, index) in faqs"
                            :key="faq.id"
                            class="bg-white rounded-lg shadow-md">
                            <button
                                class="w-full px-6 py-4 text-left flex justify-between items-center"
                                @click="toggleQuestion(index)">
                                <span>{{ faq.title }}</span>
                                <span
                                    class="transform transition-transform"
                                    :class="{ 'rotate-180': openQuestions[index] }">
                                    ▼
                                </span>
                            </button>
                            <div v-show="openQuestions[index]" class="px-6 pb-4">
                                {{ faq.content }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import { RouterLink } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'

import manualIcon from '@/assets/icons/manual.png'
import documentIcon from '@/assets/icons/documentos.png'
import { useFaqStore } from '@/stores/ajuda/faq.store'
import type { Faq } from '@/types/ajuda.types'
import { onMounted } from 'vue'

const faqStore = useFaqStore()

const faqs = ref<Faq[]>([])


onMounted( async () =>{
    try{
        await faqStore.fetchFaqs()
        faqs.value = faqStore.faqs
        console.log('FAQs:', faqs)
    }catch (error){
        console.error("Erro ao buscar dados", error)
    }
})

const openQuestions = ref(new Array(faqs.value.length).fill(false))

const toggleQuestion = (index: number) => {
    openQuestions.value[index] = !openQuestions.value[index]
}
</script>

<style scoped>
.bg-white {
    @apply transition-all duration-200;
}

.bg-white:hover {
    @apply shadow-lg;
}
</style>
