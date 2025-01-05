import type { Contato } from "@/types/contato.types";

export async function fetchContatos(): Promise<Contato[]>{
    const url = 'http://172.105.155.145/api/institucional/contato/';

    try{
        const response = await fetch(url)

        if(!response.ok){
            throw new Error(`HTTP error! Status: ${response.status}`)
        }
        const data: Contato[] = await response.json();
        return data;   
    } catch (error){
        console.error('Erro ao buscar contatos:',error);
        throw error
    }

}

export async function fetchContatoById(id: string): Promise<Contato> {
    const url = `http://172.105.155.145/api/institucional/contato/${id}`;

    try{
        const response = await fetch(url);

        if(!response.ok){
            throw new Error(`HTTP error! Satatus: ${response.status}`)
        }

        const data: Contato = await response.json();
        return data;
    } catch (error){
        console.error('Erro ao buscar contato:', error);
        throw error;
    }
}

export async function submitContato(formData: Contato): Promise<void>{
    const url = 'http://172.105.155.145/api/institucional/contato/';
    try{
        const response = await fetch(url,{
            method:'POST', 
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });
        if(!response.ok){
            throw new Error(`Erro ao enviar dados! Status: ${response.status}`);
        }

        console.log("Dados enviados com sucesso!")


        
    } catch (error){
        console.error('Erro ao enviar o formulário:', error);
        throw error;
    }

    
}