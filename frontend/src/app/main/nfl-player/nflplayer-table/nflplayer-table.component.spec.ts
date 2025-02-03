import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NflplayerTableComponent } from './nflplayer-table.component';

describe('NflplayerTableComponent', () => {
  let component: NflplayerTableComponent;
  let fixture: ComponentFixture<NflplayerTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NflplayerTableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NflplayerTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
