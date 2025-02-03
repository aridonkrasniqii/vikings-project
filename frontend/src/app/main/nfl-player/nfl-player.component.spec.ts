import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NflPlayerComponent } from './nfl-player.component';

describe('NflPlayerComponent', () => {
  let component: NflPlayerComponent;
  let fixture: ComponentFixture<NflPlayerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NflPlayerComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NflPlayerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
