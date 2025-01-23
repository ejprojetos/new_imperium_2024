import type { FluxoDeTrabalho } from "@/types/institucional.types";
import { fetcher } from "./fetcher.service";


export const fluxoService = {
    getFluxo: () => fetcher<FluxoDeTrabalho[]>('/institucional/fluxo/'),


    submitFluxo: (data: FormData) => 
        fetcher<FluxoDeTrabalho>('/institucional/fluxo/', {
            method: 'POST',
            body: data
    }),

    updateFluxo: (id: string, data: FormData) =>
        fetcher(`/institucional/fluxo/${id}/`, {
            method: 'PUT',
            body: data
        })
}