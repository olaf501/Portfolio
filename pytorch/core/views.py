from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    context = {
        'name': 'GARCIA, OLAF IZAHK M.',
        'bio': 'Engineer operating at the intersection of complex software systems, hardware architecture, and intelligent computing.',
        'skills': {
            'Languages': 'Python, C++, Verilog, VHDL, GLSL/HLSL, SQL',
            'Game Dev': 'Unreal Engine, Unity, Physics Engines, Graphics Pipelines',
            'VLSI & Chip Design': 'RTL Coding, Logic Synthesis, Static Timing Analysis (STA), FPGA',
            'Artificial Intelligence': 'PyTorch, TensorFlow, CNNs, Reinforcement Learning, Core Math'
        },
        'projects': projects
    }
    return render(request, 'core/home.html', context)