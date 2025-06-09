import { manualService } from "@/services/ajuda.service";
import { defineStore } from "pinia";
import { computed, ref } from "vue";





export const useManualStore = defineStore('manual', () => {
    const manuals = ref<Manual[]>([]);
    const currentManual = ref<Manual | null>(null);
    const loading = ref(false);
    const error = ref<string | null>(null);


    const count = ref(0);
    const next = ref<string | null>(null);
    const previous = ref<string | null>(null);


    //novos estados para paginação
    const totalCount = ref(0);
    const currentPage = ref(1);
    const pageSize = ref(5);
    const totalPages = computed(() => Math.ceil(totalCount.value / pageSize.value));

    const fetchManuals = async (page = 1) => {
        try {
            loading.value = true;
            const response = await manualService.getAllManuals(page);
            manuals.value = response?.results || [];
            count.value = response?.count || 0;
            next.value = response?.next || null;
            previous.value = response?.previous || null;
            currentPage.value = page;

            return response;
        } catch (err) {
            error.value = 'Erro ao buscar manuais';
            console.error(err);
            return null;
        } finally {
            loading.value = false;
        }
    };

    const fetchSingleManual = async (id: string) => {
        try {
            loading.value = true;
            currentManual.value = await manualService.getManual(id);
        } catch (err) {
            error.value = 'Erro ao buscar manual';
            console.error(err);
        } finally {
            loading.value = false;
        }
    };

    const createManual = async (manualData: { titulo: string; profile: string; manual_archive: File }) => {
        try {
            loading.value = true;
            console.log("enviando manual para api:" , manualData);
    
            const formattedData = {
                titulo: manualData.titulo,
                profile: manualData.profile,
                manual_archive: manualData.manual_archive
            };
    
            const newManual = await manualService.createManual(formattedData);
            if (newManual) {
                manuals.value.push(newManual);
                console.log('Manual criado com sucesso:', newManual);
            }
            
            return newManual;
        } catch (err) {
            error.value = 'Erro ao criar manual';
            console.error(err);
        } finally {
            loading.value = false;
        }
    };

    const updateManual = async (id: string, manualData: { title?: string; profile?: string; manual_archive?: File, creation_date?: string }) => {
        try {
            loading.value = true;
            const updatedManual = await manualService.updateManual(id, manualData);

            if (!updatedManual) {
                throw new Error('Erro ao atualizar manual');
            }

            const index = manuals.value.findIndex(manual => manual.id === id);
            if (index !== -1) {
                manuals.value[index] = updatedManual;
            }

            return updatedManual;
        } catch (err) {
            error.value = 'Erro ao atualizar manual';
            console.error(err);
        } finally {
            loading.value = false;
        }
    };

    const deleteManual = async (id: string) => {
        try {
            loading.value = true;
            await manualService.deleteManual(id);
            manuals.value = manuals.value.filter(manual => manual.id !== id);
        } catch (err) {
            error.value = 'Erro ao deletar manual';
            console.error(err);
        } finally {
            loading.value = false;
        }
    };

    const resetCurrentManual = () => {
        currentManual.value = null;
    };
    console.log(totalCount.value, currentPage.value, pageSize.value, totalPages.value);
    return {
        manuals,
        count,
        next,
        previous,
        currentManual,
        loading,
        error,
        totalCount,
        currentPage,
        pageSize,
        totalPages,
        fetchManuals,
        fetchSingleManual,
        createManual,
        updateManual,
        deleteManual,
        resetCurrentManual
    };
});
