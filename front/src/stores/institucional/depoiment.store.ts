import { defineStore } from "pinia";
import { ref } from "vue";
import { depoimentoService } from "@/services/depoimentos.service";
import type { Depoimento } from "@/types/institucional.types";


export const useDepoimentoStore = defineStore("depoimento", () => {
    const depoimentos = ref<Depoimento[]>([]);
    const currentDepoimento = ref<Depoimento | null>(null);
    const loading = ref(false);
    const error = ref<string | null>(null);

    const fetchDepoimentos = async () => {
        try{
            loading.value = true;
            if (!depoimentos.value.length) {
                depoimentos.value = await depoimentoService.getAllDepoimentos();
            }
        } catch (err) {
            error.value = "Erro ao buscar depoimentos";
            console.error(err);
        }finally{
            loading.value = false;
        }
    }

    const fetchSingleDepoimento = async (id: string) => {
        try {
            loading.value = true;
            currentDepoimento.value = await depoimentoService.getDepoimento(id);
        } catch (err) {
            error.value = "Erro ao buscar depoimento";
            console.error(err);
        } finally {
            loading.value = false;
        }
    }

    const createDepoimento = async ( depoimentoData: FormData) => {
        try {
            loading.value = true;
            const newDepoimento = await depoimentoService.submitDepoimento(depoimentoData);
            depoimentos.value.push(newDepoimento);
            return newDepoimento;
        } catch (err) {
            error.value = "Erro ao criar depoimento";
            console.error(err);
            throw err;
        } finally {
            loading.value = false;
        }
    }

    const updateDepoimento = async (id: string, depoiementoData: FormData) => {
        try {
            loading.value = true;
            const updatedDepoimento = await depoimentoService.updateDepoimento(id, depoiementoData);
            const index = depoimentos.value.findIndex((d) => d.id === id);
            if (index !== -1) {
                depoimentos.value[index] = updatedDepoimento as Depoimento;
            }

            return updatedDepoimento;
        } catch (err) {
            error.value = "Erro ao atualizar depoimento";
            console.error(err);
            throw err;
        } finally {
            loading.value = false;
        }
    }

    const deleteDepoimento = async (id: string) => {
        try {
            loading.value = true;
            await depoimentoService.deleteDepoimento(id);
            depoimentos.value = depoimentos.value.filter((d) => d.id !== id);
        } catch (err) {
            error.value = "Erro ao deletar depoimento";
            console.error(err);
            throw err;
        } finally {
            loading.value = false;
        }
    }

    const resetCurrentDepoimento = () => {
        currentDepoimento.value = null;
    };

    return{
        depoimentos,
        currentDepoimento,
        loading,
        error,
        fetchDepoimentos,
        fetchSingleDepoimento,
        createDepoimento,
        updateDepoimento,
        resetCurrentDepoimento,
        deleteDepoimento
    };
});


