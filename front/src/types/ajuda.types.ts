interface Faq {
    id: number
    title: string
    questions: string
    content: string
    profile: string
    tags: {
        id: number
        name: string
    }[]
}


interface Policies {
    id: number
    profile: string
    title: string
    content: string
}

interface Manual {
    id: string
    title: string
    profile: string
    manual_archive: string
    date_created: string
}