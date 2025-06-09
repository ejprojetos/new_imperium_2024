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
    // getAllManuals: () => fetcher<Manual[]>('/user-supports/'),

    getAllManuals: (page = 1) => fetcher<{
        results: Manual[];
        count: number;
        next: string | null;
        previous: string | null;
    }>('/user-supports/?page=' + page),

    getManual: (id: string) => fetcher<Manual>(`/user-supports/${id}/`),

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
    

    
    updateManual: (id: string, data: {
    title?: string;
    profile?: string;
    manual_archive?: File;
    creation_date?: string;
  }) => {
    const formData = new FormData();
    if (data.title)           formData.append('title', data.title);
    if (data.profile)         formData.append('profile', data.profile);
    if (data.manual_archive)  formData.append('manual_archive', data.manual_archive);
    if (data.creation_date)   formData.append('creation_date', data.creation_date);

    return fetcher<Manual>(`/user-supports/${id}/`, {
      method: 'PATCH',
      body: formData,
    });
  },

    deleteManual: (id: number) => fetcher(`/manuals/${id}/`, { method: 'DELETE' })

}

