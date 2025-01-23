export interface Depoimento{
    id: string;
    nome: string;
    depoimento: string;
    imagem: string;
    ativo?: boolean;
}

export interface PaginaInicial{
    id: string
    uuid: string;
    frase: string;
    imagem: string;
}


export interface FluxoDeTrabalho{
    id: string;
    uuid: string;
    titulo1: string;
    descricao1: string;
    imagem1: string;
    titulo2: string;
    descricao2: string;
    imagem2: string;
    titulo3: string;
    descricao3: string;
    imagem3: string;
    titulo4: string;
    descricao4: string;
    imagem4: string;
}

export interface Feature {
    uuid:string;
    id: string;
    titulo1: string;
    descricao1: string
    imagem1: string;  
    titulo2: string;
    descricao2: string;
    imagem2: string;
    titulo3: string;
    descricao3: string;
    imagem3: string;
    titulo4: string;
    descricao4: string;
    imagem4: string;
    titulo5: string;
    descricao5: string;
    imagem5: string;
}

export interface Contato{
    id:string
    nome: string
    telefone: string
    email: string
    assunto: string
    mensagem: string
    respondido: boolean
    respondido_data: string
    envio_data: string
}