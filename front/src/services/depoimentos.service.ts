import type { Depoimento } from "@/types/institucional.types";
import { fetcher } from "./fetcher.service";


export const depoimentoService = {
    //buscar todos os depoimentos
    getAllDepoimentos:() => fetcher<Depoimento[]>('/institucional/depoimento/'),

    //buscar pelo id
    getDepoimento: (id: string) => fetcher<Depoimento>(`/institucional/depoimento/${id}`),

    //criar novo depoimento
    submitDepoimento:(data: FormData) =>
        fetcher<Depoimento>('/institucional/depoimento/', {
            method: 'POST',
            body: data
        }),

    //editar depoimento
    updateDepoimento:(id: string, data:FormData) =>
        fetcher(`/institucional/depoimento/${id}/`,{
            method:'PUT',
            body:data
        }),

    //delete depoimento
    deleteDepoimento:(id: string) =>
        fetcher(`/institucional/depoimento/${id}/`,{
            method:'DELETE'
        })
}
