export class BackendNFLPlayer {
  id: number;
  number: number;
  position: string;
  age: number;
  experience: number;
  college: string;
  name: string;
  photo: string;
  stats: BackendNFLPlayerStats[];
  created_at: string;
  updated_at: string;

  constructor(init?: Partial<BackendNFLPlayer>) {
    Object.assign(this, init);
  }
}

export class BackendNFLPlayerStats {
  id: number;
  player_id: number;
  season: number;
  team: string;
  games_played: number;
  receptions: number;
  receiving_yards: number;
  receiving_touchdowns: number;
  longest_reception: number;

  constructor(init?: Partial<BackendNFLPlayerStats>) {
    Object.assign(this, init);
  }
}

export class FrontendNFLPlayer {
  id: number;
  number: number;
  position: string;
  age: number;
  experience: number;
  college: string;
  name: string;
  photo: string;
  stats: FrontendNFLPlayerStats[];
  createdAt: string;
  updatedAt: string;

  constructor(init?: Partial<FrontendNFLPlayer>) {
    Object.assign(this, init);
  }

  static fromBackend(backendPlayer: BackendNFLPlayer): FrontendNFLPlayer {
    return new FrontendNFLPlayer({
      id: backendPlayer.id,
      number: backendPlayer.number,
      position: backendPlayer.position,
      age: backendPlayer.age,
      experience: backendPlayer.experience,
      college: backendPlayer.college,
      name: backendPlayer.name,
      photo: backendPlayer.photo,
      stats: backendPlayer.stats.map(stat => FrontendNFLPlayerStats.fromBackend(stat)),
      createdAt: backendPlayer.created_at,
      updatedAt: backendPlayer.updated_at
    });
  }

  static toBackend(frontendPlayer: FrontendNFLPlayer): BackendNFLPlayer {
    return new BackendNFLPlayer({
      id: frontendPlayer.id,
      number: frontendPlayer.number,
      position: frontendPlayer.position,
      age: frontendPlayer.age,
      experience: frontendPlayer.experience,
      college: frontendPlayer.college,
      name: frontendPlayer.name,
      photo: frontendPlayer.photo,
      stats: frontendPlayer.stats.map(stat => FrontendNFLPlayerStats.toBackend(stat)),
      created_at: frontendPlayer.createdAt,
      updated_at: frontendPlayer.updatedAt
    });
  }
}

export class FrontendNFLPlayerStats {
  id: number;
  playerId: number;
  season: number;
  team: string;
  gamesPlayed: number;
  receptions: number;
  receivingYards: number;
  receivingTouchdowns: number;
  longestReception: number;

  constructor(init?: Partial<FrontendNFLPlayerStats>) {
    Object.assign(this, init);
  }

  static fromBackend(backendStats: BackendNFLPlayerStats): FrontendNFLPlayerStats {
    return new FrontendNFLPlayerStats({
      id: backendStats.id,
      playerId: backendStats.player_id,
      season: backendStats.season,
      team: backendStats.team,
      gamesPlayed: backendStats.games_played,
      receptions: backendStats.receptions,
      receivingYards: backendStats.receiving_yards,
      receivingTouchdowns: backendStats.receiving_touchdowns,
      longestReception: backendStats.longest_reception
    });
  }

  static toBackend(frontendStats: FrontendNFLPlayerStats): BackendNFLPlayerStats {
    return new BackendNFLPlayerStats({
      id: frontendStats.id,
      player_id: frontendStats.playerId,
      season: frontendStats.season,
      team: frontendStats.team,
      games_played: frontendStats.gamesPlayed,
      receptions: frontendStats.receptions,
      receiving_yards: frontendStats.receivingYards,
      receiving_touchdowns: frontendStats.receivingTouchdowns,
      longest_reception: frontendStats.longestReception
    });
  }
}
