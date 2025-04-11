import { manualService } from "@/services/ajuda.service";
import { defineStore } from "pinia";
import { ref } from "vue";





export const useManualStore = defineStore('manual', () => {
    const manuals = ref<Manual[]>([]);
    const currentManual = ref<Manual | null>(null);
    const loading = ref(false);
    const error = ref<string | null>(null);

    const fetchManuals = async () => {
        try {
            loading.value = true;
            manuals.value = (await manualService.getAllManuals()) || [];
        } catch (err) {
            error.value = 'Erro ao buscar manuais';
            console.error(err);
        } finally {
            loading.value = false;
        }
    };

    const fetchSingleManual = async (id: number) => {
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

    const updateManual = async (id: number, manualData: { titulo?: string; perfil?: string; manual?: File }) => {
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

    const deleteManual = async (id: number) => {
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

    return {
        manuals,
        currentManual,
        loading,
        error,
        fetchManuals,
        fetchSingleManual,
        createManual,
        updateManual,
        deleteManual
    };
});
