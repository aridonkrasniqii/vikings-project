export class BackendNorseman {
    id: number;
    name: string;
    photo: string;
    actor_name: string;
    description: string;
    created_at: string;
    updated_at: string;
  
    constructor(init?: Partial<BackendNorseman>) {
      Object.assign(this, init);
    }
  }
  
export class FrontendNorseman {
    id: number;
    name: string;
    photo: string;
    actorName: string;
    description: string;
    createdAt: string;
    updatedAt: string;
  
    constructor(init?: Partial<FrontendNorseman>) {
      Object.assign(this, init);
    }
  
    static fromBackend(backendNorseman: BackendNorseman): FrontendNorseman {
      return new FrontendNorseman({
        id: backendNorseman.id,
        name: backendNorseman.name,
        photo: backendNorseman.photo,
        actorName: backendNorseman.actor_name,
        description: backendNorseman.description,
        createdAt: backendNorseman.created_at,
        updatedAt: backendNorseman.updated_at
      });
    }
  
    static toBackend(frontendNorseman: FrontendNorseman): BackendNorseman {
      return new BackendNorseman({
        id: frontendNorseman.id,
        name: frontendNorseman.name,
        photo: frontendNorseman.photo,
        actor_name: frontendNorseman.actorName,
        description: frontendNorseman.description,
        created_at: frontendNorseman.createdAt,
        updated_at: frontendNorseman.updatedAt
      });
    }
  }
  