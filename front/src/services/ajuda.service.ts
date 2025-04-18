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