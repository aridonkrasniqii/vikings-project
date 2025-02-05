import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { NFLPlayerService } from '../../../services/nfl-player.service';
import { FrontendNFLPlayer, FrontendNFLPlayerStats } from '../../../models/nfl-players.model';

@Component({
  standalone: false,
  selector: 'app-nflplayer-form',
  templateUrl: './nflplayer-form.component.html',
  styleUrls: ['./nflplayer-form.component.css']
})
export class NFLPlayerFormComponent implements OnInit {
  playerForm: FormGroup;
  formStatus: { type: string; message: string } | null = null;

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private playerService: NFLPlayerService
  ) {}

  ngOnInit(): void {
    this.initForm();
  }

  initForm(): void {
    this.playerForm = this.fb.group({
      name: ['', Validators.required],
      number: ['', Validators.required],
      position: ['', Validators.required],
      age: ['', Validators.required],
      experience: ['', Validators.required],
      college: ['', Validators.required],
      photo: ['', Validators.required],
      stats: this.fb.array([this.createStatFormGroup()]) // Initialize with one stat form group
    });
  }

  get stats(): FormArray {
    return this.playerForm.get('stats') as FormArray;
  }

  createStatFormGroup(): FormGroup {
    return this.fb.group({
      season: ['', Validators.required],
      team: ['', Validators.required],
      gamesPlayed: ['', Validators.required],
      receptions: ['', Validators.required],
      receivingYards: ['', Validators.required],
      receivingTouchdowns: ['', Validators.required],
      longestReception: ['', Validators.required]
    });
  }

  addStat(): void {
    this.stats.push(this.createStatFormGroup());
  }

  removeStat(index: number): void {
    this.stats.removeAt(index);
  }

  onSubmit(): void {
    if (this.playerForm.invalid) {
      return;
    }

    const newPlayer = new FrontendNFLPlayer({
      name: this.playerForm.value.name,
      number: this.playerForm.value.number,
      position: this.playerForm.value.position,
      age: this.playerForm.value.age,
      experience: this.playerForm.value.experience,
      college: this.playerForm.value.college,
      photo: this.playerForm.value.photo,
      stats: this.playerForm.value.stats.map((stat: any) => new FrontendNFLPlayerStats(stat))
    });

    this.playerService.createNFLPlayer(newPlayer).subscribe({
      next: () => {
        this.formStatus = { type: 'success', message: 'Player created successfully!' };
        setTimeout(() => {
          this.formStatus = null;
          this.router.navigate(['/nflplayers']);
        }, 2000);
      },
      error: (error) => {
        this.formStatus = { type: 'error', message: `Creation failed: ${error.message}` };
      }
    });
  }

  goBack(): void {
    this.router.navigate(['/nflplayers']);
  }
}
