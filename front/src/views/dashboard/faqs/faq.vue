<template>
    <LayoutDashboard>
        <div class="container mx-auto px-4 py-8">
            <h1 class="text-2xl font-bold text-center text-blue-900 mb-12">Suporte ao usuário</h1>

            <!-- <Escolher_perfil @setPerfil="handlePerfilSelecionado" /> -->


            <div class="max-w-4xl mx-auto">
                <!-- Resources Section -->
                <div class="bg-white rounded-lg shadow-md p-6 mb-8 grid grid-cols-2 gap-8">
                    <div>
                        <a :href="manualUsuarioDownload" class="flex flex-col items-center hover:opacity-80 transition-opacity" target="_blank" rel="noopener noreferrer">
                            <img :src="manualIcon" alt="Manual" class="w-16 h-16 mb-2" />
                            <span class="text-blue-900">Manual do usuário</span>
                        </a>
                    </div>

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
                            v-for="(faq, index) in filteredFaqs"
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
import { computed, reactive, ref } from 'vue'
import { RouterLink } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'

import manualIcon from '@/assets/icons/manual.png'
import documentIcon from '@/assets/icons/documentos.png'
import { useFaqStore } from '@/stores/ajuda/faq.store'
import type { Faq } from '@/types/ajuda.types'
import { onMounted } from 'vue'


const userStore = useUserStore()
const { role } = storeToRefs(userStore)

const faqStore = useFaqStore()

const faqs = ref<Faq[]>([])

const manualStore = useManualStore()


//const manualUsuarioDownload = ref('')

const manualUsuarioDownload = computed(() =>{
    const manuais = manualUsuario.value
    return manuais.length > 0 ? manuais[manuais.length - 1].manual_archive : ''
})

import { perfilSelecionado } from '@/stores/ajuda/perfilStore'
import { useUserStore } from '@/stores/user/useUserStore'
import { storeToRefs } from 'pinia'
import { useManualStore } from '@/stores/ajuda/manualStore'


const filteredFaqs = computed(() => {
    return faqs.value.filter((faq: { profile: string }) => faq.profile === perfilSelecionado.value)
})

onMounted( async () =>{
    try{
        await faqStore.fetchFaqs()
        faqs.value = faqStore.faqs
        console.log('FAQs:', faqs)
        console.log(role.value)

        await manualStore.fetchManuals()
        console.log(manualStore.manuals.length)
        console.log(manualStore.manuals[0].manual_archive)

    }catch (error){
        console.error("Erro ao buscar dados", error)
    }
})

const manualUsuario = computed(() =>{
    return manualStore.manuals.filter((manual) =>
        manual.profile === role.value
    )

})
console.log("manualUsuario",manualUsuario.value)


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
