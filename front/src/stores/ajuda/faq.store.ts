import { ajudaService } from "@/services/ajuda.service"
import type { Faq } from "@/types/ajuda.types"
import { defineStore } from "pinia"
import { ref } from "vue"



export const useFaqStore = defineStore('faq', () => {
    const faqs = ref<Faq[]>([])
    const currentFaq = ref<Faq | null>(null)
    const loading = ref(false)
    const error = ref<string | null>(null)

    const fetchFaqs = async () => {
        try {
            loading.value = true
            const response = await ajudaService.getAllFaqs()
            if(response && response.results){
                faqs.value = response.results
                console.log(faqs)
            }
            
        } catch (err) {
            error.value = 'Erro ao buscar faqs'
            console.error(err)
        } finally {
            loading.value = false
        }
    }

    const fetchSingleFaq = async (id: number) => {
        try {
            loading.value = true
            currentFaq.value = await ajudaService.getFaq(id)
        } catch (err) {
            error.value = 'Erro ao buscar faq'
            console.error(err)
        } finally {
            loading.value = false
        }
    }

    const createFaq = async (faqData: Partial<Faq>) => {
        try {
            loading.value = true
            const newFaq = await ajudaService.createFaq(faqData)
            faqs.value.push(newFaq)
            return newFaq
        } catch (err) {
            error.value = 'Erro ao criar faq'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }
    }

    const updateFaq = async (id: number, faqData: Partial<Faq>) => {
        try {
            loading.value = true

            const updatedFaq = await ajudaService.updateFaq(id, faqData)

            if(!updatedFaq) {
                throw new Error('Erro ao atualizar faq')
            }

            const index = faqs.value.findIndex(faq => faq.id === id)
            faqs.value[index] = updatedFaq

            return updatedFaq
        } catch (err) {
            error.value = 'Erro ao atualizar faq'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }
    }

    const deleteFaq = async (id: number) => {
        try {
            loading.value = true
            await ajudaService.deleteFaq(id)
            faqs.value = faqs.value.filter(faq => faq.id !== id)
        } catch (err) {
            error.value = 'Erro ao deletar faq'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }
    }


    return {
        faqs,
        currentFaq,
        loading,
        error,
        fetchFaqs,
        fetchSingleFaq,
        createFaq,
        updateFaq,
        deleteFaq
    }

})