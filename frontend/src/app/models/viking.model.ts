export class BackendViking {
    id: number;
    name: string;
    photo: string;
    actor_name: string;
    description: string;
    created_at: string;
    updated_at: string;
  
    constructor(init?: Partial<BackendViking>) {
      Object.assign(this, init);
    }
  }
  
  
  export class FrontendViking {
    id: number;
    name: string;
    photo: string;
    actorName: string;
    description: string;
    createdAt: string;
    updatedAt: string;
  
    constructor(init?: Partial<FrontendViking>) {
      Object.assign(this, init);
    }
  
    static fromBackend(backendViking: BackendViking): FrontendViking {
      return new FrontendViking({
        id: backendViking.id,
        name: backendViking.name,
        photo: backendViking.photo,
        actorName: backendViking.actor_name,
        description: backendViking.description,
        createdAt: backendViking.created_at,
        updatedAt: backendViking.updated_at
      });
    }
  
    static toBackend(frontendViking: FrontendViking): BackendViking {
      return new BackendViking({
        id: frontendViking.id,
        name: frontendViking.name,
        photo: frontendViking.photo,
        actor_name: frontendViking.actorName,
        description: frontendViking.description,
        created_at: frontendViking.createdAt,
        updated_at: frontendViking.updatedAt
      });
    }
  }
  