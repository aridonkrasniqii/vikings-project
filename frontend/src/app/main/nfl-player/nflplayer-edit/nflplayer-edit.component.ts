import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { NFLPlayerService } from '../../../services/nfl-player.service';
import { FrontendNFLPlayer } from '../../../models/nfl-players.model';


@Component({
  standalone: false,
  selector: 'app-nflplayer-edit',
  templateUrl: './nflplayer-edit.component.html',
  styleUrls: ['./nflplayer-edit.component.css']
})
export class NFLPlayerEditComponent implements OnInit {
  editForm: FormGroup;
  playerId: number;
  nflPlayer: FrontendNFLPlayer;
  formStatus: { type: string; message: string } | null = null;
  loading: boolean = true;
  updateSuccess: boolean | null = null; 

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private playerService: NFLPlayerService
  ) {}

  ngOnInit(): void {
    this.playerId = +this.route.snapshot.paramMap.get('id');
    this.createForm();
    this.loadPlayer();
  }

  createForm(): void {
    this.editForm = this.fb.group({
      name: ['', Validators.required],
      number: ['', Validators.required],
      position: ['', Validators.required],
      age: ['', Validators.required],
      experience: ['', Validators.required],
      college: ['', Validators.required],
      photo: ['', Validators.required ] // Validators.pattern('https?://.+')]
    });
  }

  loadPlayer(): void {
    this.playerService.getNFLPlayerById(this.playerId).subscribe({
      next: (response) => {
        if (response && response.data) {
          this.nflPlayer = FrontendNFLPlayer.fromBackend(response.data[0]);
          this.editForm.patchValue(this.nflPlayer);
        }
        this.loading = false;
      },
      error: (error) => {
        console.error('Error loading player:', error);
        this.formStatus = { type: 'error', message: `Failed to load player: ${error.message}` };
        this.loading = false;
      }
    });
  }

  onSubmit(): void {
    if (this.editForm.invalid) {
      return;
    }

    this.updatePlayer();
  }

  private updatePlayer() { 
    const updatedPlayer = new FrontendNFLPlayer({
      name: this.editForm.value.name,
      number: this.editForm.value.number,
      position: this.editForm.value.position,
      age: this.editForm.value.age,
      experience: this.editForm.value.experience,
      college: this.editForm.value.college,
      photo: this.editForm.value.photo
    });

    this.playerService.updateNFLPlayer(this.playerId, updatedPlayer).subscribe({
      next: () => {
        this.updateSuccess = true;
        this.formStatus = { type: 'success', message: 'Player updated successfully!' };
        setTimeout(() => {
          this.router.navigate(['/nflplayers']);
        }, 2000);
      },
      error: (error) => {
        this.updateSuccess = false;
        this.formStatus = { type: 'error', message: `Update failed: ${error.message}` };
      }
    });
  }
}
