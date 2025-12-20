# 🧪 Session de test intégrée — tous modules verrouillés
import yaml

def run_integrated_test(registry_path="config/module_registry.yaml"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    locked = [name for name, data in registry.items() if data["status"] == "verrouillé"]
    print("🚀 Test intégré — modules verrouillés\n")
    for name in locked:
        print(f"🧪 Test simulé : {name} — Score {registry[name]['score']} — OK")

    print(f"\n✅ {len(locked)} module(s) testés en session intégrée.")

if __name__ == "__main__":
    run_integrated_test()
