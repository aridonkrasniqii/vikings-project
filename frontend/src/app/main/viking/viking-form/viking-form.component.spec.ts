import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VikingFormComponent } from './viking-form.component';

describe('VikingFormComponent', () => {
  let component: VikingFormComponent;
  let fixture: ComponentFixture<VikingFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VikingFormComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VikingFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
