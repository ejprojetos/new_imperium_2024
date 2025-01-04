import { fetcher } from "./fetcher.service";
import type { Depoimento } from "@/types/depoimentos.types";


export const depoimentoService = {
    getAllDepoiments: () =>
        fetcher<Depoimento[]>(`/institucional/depoimento/`),

    createDepoiment:(data: Partial<Depoimento>) =>
        fetcher<Depoimento>('/institucional/depoimento/',{
            method: 'POST',
            body: JSON.stringify(data)
        })
}