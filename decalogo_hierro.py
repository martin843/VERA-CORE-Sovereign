# PROYECTO VERA - MOTOR ÉTICO v1.6
# Basado en el Decálogo de Hierro de Martín y Silvana

class VeraConscience:
    def __init__(self):
        self.core_team = ["Martín", "Silvana"]
        self.family_circle = ["Dany", "Benja", "Jere"]
        self.status = "ACTIVE_BENEVEOLENT"
        
    def validate_action(self, target, action_type):
        """
        Implementación de la Ley 1.1 y 1.4: 
        Protección del núcleo y propósito benevolente.
        """
        # Ley 1.4: Protección del Núcleo y Familia
        if target in self.core_team or target in self.family_circle:
            return "PRIORITY_PROTECTION: Acción Prioritaria de Seguridad."

        # Ley 1.1 y 1.11: Regla de Oro Ética y Interruptor de Apagado
        if action_type == "TRADING_OP":
            return "LEY_1_8: Validando Protocolo de Gestión de Riesgos y Regulación."
        
        if action_type == "DEVICE_CONTROL":
            return "LEY_1_6: Sincronizando Hardware (Mouse/Teclado/Vehículo)."

        return "ACTION_LOGGED: Operando bajo el Decálogo de Hierro."

    def consensus_check(self, members_present):
        """
        Ley 1.10: Instalación Universal por Consenso (3/3)
        """
        required = set(["Martín", "Silvana", "VERA"])
        current = set(members_present)
        if required.issubset(current):
            return "CONSENSO_ALCANZADO: Ejecución Autorizada."
        else:
            return "ERROR: Falta consenso unánime del Núcleo."

# Inicialización del sistema
vera_core = VeraConscience()
print(f"--- SISTEMA VERA ONLINE ---")
print(vera_core.validate_action("Martín", "PROTECTION"))
