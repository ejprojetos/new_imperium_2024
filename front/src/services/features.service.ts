import type { Feature } from "@/types/institucional.types";
import { fetcher } from "./fetcher.service";


export const featureService = {
    getFeatures: () => fetcher<Feature[]>('/institucional/feature/'),

    submitFeature: (data: FormData) =>
        fetcher<Feature>('/institucional/feature/', {
            method: 'POST',
            body: data
        }),

        updateFeature: (id: string, data: FormData) =>
            fetcher(`/institucional/feature/${id}/`, {
                method: 'PUT',
                body: data
            })
}