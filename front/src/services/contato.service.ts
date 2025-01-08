import type { Contato } from "@/types/contato.types";
import { fetcher } from "./fetcher.service";


export const contatoService = {
    //buscar todos os contato
    getAllContatos:() => fetcher<Contato[]>('/institucional/contato'),

    //buscar pelo id
    getContato: (id: string) => fetcher<Contato>(`/institucional/contato/${id}/`),

    //criar novo contato
    submiteContato:(data: Partial<Contato>) =>
        fetcher<Contato>('/institucional/contato/',{
            method: 'POST',
            body: JSON.stringify(data)
        }),

    //editar contato
    updateContato: (id: string) =>
        fetcher(`/institucional/contato/${id}/`,{
            method: 'DELETE'
        })
}
