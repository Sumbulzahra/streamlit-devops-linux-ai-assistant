import psutil
import platform
import sys
import subprocess

def get_complete_devops_context():
    # System & Python details
    sys_info = f"OS: {platform.system()} {platform.release()} | Python Version: {sys.version.split()[0]}"
    
    # CPU & RAM Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    # Top 5 Processes (Windows / System)
    processes = []
    for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Sort top processes by CPU usage
    top_proc = sorted(processes, key=lambda p: p['cpu_percent'] or 0, reverse=True)[:5]
    proc_summary = ", ".join([f"{p['name']} (CPU: {p['cpu_percent']}%, RAM: {round(p['memory_percent'] or 0, 1)}%)" for p in top_proc])
    
    # Docker Status Check
    try:
        docker_check = subprocess.run(["docker", "ps"], capture_output=True, text=True, timeout=3)
        if docker_check.returncode == 0:
            docker_status = "Docker is running active containers."
        else:
            docker_status = "Docker service is not running or permission denied."
    except Exception:
        docker_status = "Docker command not available or not installed."

    return f"""
    [System & DevOps Environment State]
    {sys_info}
    CPU Usage: {cpu_usage}%
    RAM Usage: {ram_usage}%
    Top Processes: {proc_summary}
    Docker Status: {docker_status}
    """
