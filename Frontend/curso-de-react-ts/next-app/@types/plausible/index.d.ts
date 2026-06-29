type Options = {
    callback?: () => void
    props: Record<string, string | number | undefined>
}

interface Window { plausible: (event: 'Add new fox' | 'Remove fox', options?: Options) => void }