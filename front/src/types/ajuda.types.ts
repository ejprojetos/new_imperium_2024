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