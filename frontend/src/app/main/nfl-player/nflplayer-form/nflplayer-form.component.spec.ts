import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NflplayerFormComponent } from './nflplayer-form.component';

describe('NflplayerFormComponent', () => {
  let component: NflplayerFormComponent;
  let fixture: ComponentFixture<NflplayerFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NflplayerFormComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NflplayerFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
