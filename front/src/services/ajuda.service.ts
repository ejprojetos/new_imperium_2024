import type { Faq } from "@/types/ajuda.types";
import { fetcher } from "./fetcher.service";


export const ajudaService = {   
    getAllFaqs: () => fetcher<Faq[]>('/faqs/'),

    getFaq: (id: number) => fetcher<Faq>(`/faqs/${id}/`),

    createFaq: (data: Partial<Faq>) =>
        fetcher<Faq>('/faqs/', {
            method: 'POST',
            body: JSON.stringify(data)
        }),
    
    updateFaq: (id: number, data: Partial<Faq>) =>
        fetcher<Faq>(`/faqs/${id}/`, {
            method: 'PUT',
            body: JSON.stringify(data)
        }),

    deleteFaq: (id: number) =>
        fetcher(`/faqs/${id}/`, {
            method: 'DELETE'
        })

}

export const policiesService = {

        getAllPolicies: () => fetcher<Policies[]>('/user-policies/'),

        getPolicy: (id: number) => fetcher<Policies>(`/user-policies/${id}/`),

        createPolicy: (data: Partial<Policies>) => 
            fetcher<Policies>('/user-policies/', {
                method: 'POST',
                body: JSON.stringify(data)
            }),

        updatePolicy: (id:number, data: Partial<Policies>) =>
            fetcher<Policies>(`/policies/${id}/`,{
                method: 'PUT',
                body: JSON.stringify(data)
            }),

        deletPolicy: (id:number) =>
            fetcher(`/policies/${id}/`, {
                method: 'DELETE'
            }) 
}

export const manualService = {
    getAllManuals: () => fetcher<Manual[]>('/user-supports/'),

    getManual: (id: number) => fetcher<Manual>(`/user-supports/${id}/`),

    createManual: (data: { titulo: string; profile: string; manual_archive: File }) => {
        if (!data.manual_archive) {
            console.error("Erro: 'manual_archive' está indefinido!");
            return Promise.reject(new Error("manual_archive está indefinido"));
        }
    
        const formData = new FormData();
        formData.append("title", data.titulo);
        formData.append("profile", data.profile);
        formData.append("manual_archive", data.manual_archive);


        try {
    
            console.log("📤 Dados enviados para API:", Object.fromEntries(formData.entries()));
    
            return fetcher<Manual>("/user-supports/", {
                method: "POST",
                body: formData,
            });
        } catch (error) {
            console.error("Erro ao converter Base64 para Blob:", error);
            return Promise.reject(error);
        }
    },
    

    
    updateManual: (id: number, data: { titulo?: string; perfil?: string; manual?: File }) => {
        const formData = new FormData();
        if (data.titulo) formData.append('title', data.titulo);
        if (data.perfil) formData.append('profile', data.perfil);
        if (data.manual) formData.append('manual_archive', data.manual);

        return fetcher<Manual>(`/user-supports/${id}/`, {
            method: 'PUT',
            body: formData
        });
    },

    deleteManual: (id: number) => fetcher(`/manuals/${id}/`, { method: 'DELETE' })

}

