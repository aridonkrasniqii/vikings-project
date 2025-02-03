import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NflplayerDetailsComponent } from './nflplayer-details.component';

describe('NflplayerDetailsComponent', () => {
  let component: NflplayerDetailsComponent;
  let fixture: ComponentFixture<NflplayerDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NflplayerDetailsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NflplayerDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
