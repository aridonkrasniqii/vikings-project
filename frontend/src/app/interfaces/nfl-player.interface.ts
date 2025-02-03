export interface NFLPlayer {
    id: number;
    number: number;
    position: string;
    age: number;
    experience: number;
    college: string;
    name: string;  
}

export interface NflPlayerStats {
    id: number;
    playerId: number;
    season: number;
    team: string;
    gamesPlayed: number;
    receptions: number;
    receivingYards: number;
    receivingTouchdowns: number;
    longestReception: number;
}
