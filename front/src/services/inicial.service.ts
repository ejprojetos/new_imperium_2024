import type { PaginaInicial } from "@/types/institucional.types";
import { fetcher } from "./fetcher.service";


export const inicialService = {
    getPaginaInicial:() => fetcher<PaginaInicial[]>('/institucional/home/'),

    
    submitDepoimento:(data: FormData) =>
        fetcher<PaginaInicial>('/institucional/home/', {
            method: 'POST',
            body:data
        }),

    updateInicial:(id:string, data:FormData) =>
        fetcher(`/institucional/home/${id}/`,{
            method:'PUT',
            body:data
        })
}

