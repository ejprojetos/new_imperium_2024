import { jwtDecode, type JwtPayload } from 'jwt-decode'

interface DecodeTokenResponse extends JwtPayload {
    user_id: number
}

export function decodeToken(token: string): DecodeTokenResponse | undefined {
    try {
        const decoded = jwtDecode<DecodeTokenResponse>(token)

        return decoded
    } catch (error) {
        console.error('Invalid JWT token', error)
    }
}
