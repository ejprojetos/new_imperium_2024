import type { Contato } from "@/types/institucional.types";
import { fetcher } from "./fetcher.service";


export const contatoService = {
    //buscar todos os contato
    getAllContatos:() => fetcher<Contato[]>('/institucional/contato/'),

    //buscar pelo id
    getContato: (id: string) => fetcher<Contato>(`/institucional/contato/${id}/`),

    //criar novo contato
    submitContato:(data: Partial<Contato>) =>
        fetcher<Contato>('/institucional/contato/',{
            method: 'POST',
            body: JSON.stringify(data)
        }),

    //editar contato
    updateContato: (id: string, data: Partial<Contato>) =>
        fetcher(`/institucional/contato/${id}/`,{
            method: 'PUT',
            body: JSON.stringify(data)
        }),


    deleteContato: (id: string) =>
        fetcher(`/institucional/contato/${id}/`,{
            method: 'DELETE'
        })
}
