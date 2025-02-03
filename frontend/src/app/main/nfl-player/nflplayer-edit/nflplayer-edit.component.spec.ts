import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NflplayerEditComponent } from './nflplayer-edit.component';

describe('NflplayerEditComponent', () => {
  let component: NflplayerEditComponent;
  let fixture: ComponentFixture<NflplayerEditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NflplayerEditComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NflplayerEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
