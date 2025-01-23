import { defineStore } from "pinia";
import { ref } from "vue";
import { contatoService } from "@/services/contato.service";
import type{ Contato } from "@/types/institucional.types";

export const useContatoStore = defineStore("contato", () => {
    const contatos = ref<Contato[]>([]);
    const currentContato = ref<Contato | null>(null);
    const loading = ref(false);
    const error = ref<string | null>(null);

    const fetchContatos = async () => {
        try {
            loading.value = true;
            if (!contatos.value.length) {
                contatos.value = await contatoService.getAllContatos();
            }
        } catch (err) {
            error.value = "Erro ao buscar contatos";
            console.error(err);
        } finally {
            loading.value = false;
        }
    }

    const fetchSingleContato = async (id: string) => {
        try {
            loading.value = true;
            currentContato.value = await contatoService.getContato(id);
        } catch (err) {
            error.value = "Erro ao buscar contato";
            console.error(err);
        } finally {
            loading.value = false;
        }
    }

    const creatContato = async (contatoData: Partial<Contato>) => {
        try {
            loading.value = true;
            const newContato = await contatoService.submitContato(contatoData);
            contatos.value.push(newContato);
            return newContato;
        } catch (err) {
            error.value = "Erro ao criar contato";
            console.error(err);
            throw err;
        } finally {
            loading.value = false;
        }
    }

    const updateContato = async (id: string, contatoData: Partial<Contato>) => {
        try {
            loading.value = true;
            const updatedContato = await contatoService.updateContato(id, contatoData);

            const index = contatos.value.findIndex((c) => c.id === id);
            if (index !== -1) {
                contatos.value[index] = updatedContato as Contato;
            }

            if(currentContato.value && currentContato.value.id === id){
                currentContato.value = updatedContato as Contato;
            }
        } catch (err) {
            error.value = "Erro ao atualizar contato";
            console.error(err);
            throw err;
        } finally {
            loading.value = false;
        }
    }

    const deleteContato = async (id: string) => {
        try {
            loading.value = true;
            await contatoService.deleteContato(id);
            contatos.value = contatos.value.filter((c) => c.id !== id);
        } catch (err) {
            error.value = "Erro ao deletar contato";
            console.error(err);
            throw err;
        } finally {
            loading.value = false;
        }
    }


    return {
        contatos,
        currentContato,
        loading,
        error,
        fetchContatos,
        fetchSingleContato,
        creatContato,
        updateContato,
        deleteContato,
    };
});