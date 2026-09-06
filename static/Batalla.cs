using Dapper;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.ComponentModel.Design.ObjectSelectorEditor;

namespace Prueba_3
{
    public partial class Batalla : Form
    {
        public List<InitiativeCreature> ini = new List<InitiativeCreature>();
        public List<Turno> turno = new List<Turno>();

        private int habiY = 10;
        private int enTipo = 0;
        private int contador = 0;
        private int turnito;

        public Batalla()
        {
            InitializeComponent();
        }
        private void Batalla_Load(object sender, EventArgs e)
        {
            this.recargarLista();
            var danios = new Modelo().tipoDanios();
            foreach (var a in danios)
            {
                this.TipoDanio.Items.Add(a.descripcion);
            }
            foreach (var b in this.turno)
            {
                this.turnito = b.numturno;
            }
            this.popularTabla();
            this.Numero.Text = this.turnito.ToString();
        }

        private void recargarLista()
        {
            this.ini = new Modelo().buscarIniciativa();
            this.turno = new Modelo().traerTurno();
        }

        private void popularTabla()
        {
            this.TablaIni.Rows.Clear();
            foreach (var c in this.ini)
            {
                DataGridViewRow dgvr = new DataGridViewRow();
                dgvr.Cells.Add(new DataGridViewTextBoxCell { Value = c.nombre });
                dgvr.Cells.Add(new DataGridViewTextBoxCell { Value = c.iniciativa });
                dgvr.Cells.Add(new DataGridViewTextBoxCell { Value = c.tipo });
                this.TablaIni.Rows.Add(dgvr);
            }
        }

        private void Turno_Click(object sender, EventArgs e)
        {
            if (contador >= ini.Count)
            {
                this.contador = 0;
                this.turnito++;
                string turn = $"UPDATE TURNO SET NUMTURNO = {this.turnito};";
                new Modelo().realizarCRUD(turn);
                this.Numero.Text = this.turnito.ToString();
            }
            string tipo = ini[contador].tipo;
            string nombre = ini[contador].nombre;
            MessageBox.Show($"Es el turno de {nombre}");
            this.contador++;
        }

        private void DatosCriatura_Paint(object sender, PaintEventArgs e)
        {

        }

        private int calcularModificador(int modificador)
        {
            return (modificador - 10) / 2;
        }

        private void TablaIni_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private int entregarNumero(string num)
        {
            try
            {
                return Convert.ToInt32(num);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Ingresa un número, no un carácter.");
                return -9999;
            }
        }
        private void Realizar_Click(object sender, EventArgs e)
        {
            int cont = 0;
            int contR = 0;
            foreach (var c in ini)
            {
                if (c.nombre == this.Nombre.Text)
                {
                    int danio = entregarNumero(this.Danio.Text);
                    if (danio != -9999)
                    {
                        List<Extra> resis = new Modelo().listarResistencia(c.idCriatura);
                        float resistencia = 0.0f;
                        foreach (var r in resis)
                        {
                            if (r.descripcion == this.TipoDanio.SelectedItem.ToString())
                            {
                                resistencia = r.cantidadR;
                                contR++;
                                break;
                            }
                        }
                        if (contR == 0)
                        {
                            resistencia = 1.0f;
                        }
                        int resultado = (int)(danio * resistencia);
                        if (resultado != -9999)
                        {
                            c.vida -= resultado;
                            string query = $"UPDATE INICIATIVA SET VIDA = {c.vida} WHERE NOMBRE = '{c.nombre}';";
                            new Modelo().realizarCRUD(query);
                            this.VidaActual.Text = $"Vida Actual: {c.vida}";
                        }
                        if (c.vida <= 0)
                        {
                            foreach (var d in ini)
                            {
                                if (c.nombre == d.nombre)
                                {
                                    ini.Remove(d);
                                    this.popularTabla();
                                    this.DatosCriatura.Visible = false;
                                    string del = $"DELETE FROM INICIATIVA WHERE NOMBRE = '{c.nombre}';";
                                    new Modelo().realizarCRUD(del);
                                    break;
                                }
                            }
                        }
                        cont++;
                        break;
                    }
                }
            }
            if (cont > 0)
            {
                MessageBox.Show("Daño realizado");
            }

        }

        private void contenedor(string texto)
        {
            System.Windows.Forms.TextBox textBox = new System.Windows.Forms.TextBox();
            textBox.Multiline = true;
            textBox.WordWrap = true;
            int maxWidth = 780;
            textBox.Width = maxWidth;
            textBox.Font = new System.Drawing.Font("Roboto Black", 13, FontStyle.Bold);
            textBox.ReadOnly = true;
            textBox.Enabled = false;
            int largoCadenaTexto = texto.Length;
            int cantidadHeight = 1 + (largoCadenaTexto / 100);
            /*string wrappedText = this.AutoWrapText(text,maxWidth,textBox); 96*/
            textBox.Text = texto;
            textBox.Location = new Point(10, this.habiY);
            textBox.Height = 25 * cantidadHeight;
            this.Container.Controls.Add(textBox);
            this.habiY += textBox.Height + 10;
        }

        private void Ver_Click(object sender, EventArgs e)
        {
            if (this.TablaIni.SelectedRows.Count > 0)
            {
                this.habiY = 10;
                DataGridViewRow fila = this.TablaIni.SelectedRows[0];
                this.Container.Controls.Clear();
                string nombre = fila.Cells[0].Value.ToString();
                string tipo = fila.Cells[2].Value.ToString();
                if (tipo == "Enemigo")
                {
                    foreach (var en in ini)
                    {
                        if (en.nombre == nombre)
                        {
                            List<Extra> salvacion = new Modelo().listarSalvacion(en.idCriatura);
                            if (salvacion.Count > 0)
                            {
                                string texto = "Tirada de Salvacion: ";
                                foreach (var d in salvacion)
                                {
                                    if (d.modificador > 0)
                                    {
                                        texto += $"| {d.descripcion}: +{d.modificador} | ";
                                    }
                                    else
                                    {
                                        texto += $"| {d.descripcion}: -{d.modificador} | ";
                                    }
                                }
                                this.contenedor(texto);
                            }
                            List<Extra> habs = new Modelo().listarHabCriat(en.idCriatura);
                            if (habs.Count > 0)
                            {
                                string texto = "Habilidades: ";
                                foreach (var d in habs)
                                {
                                    if (d.modificador > 0)
                                    {
                                        texto += $"| {d.descripcion}: +{d.modificador} | ";
                                    }
                                    else
                                    {
                                        texto += $"| {d.descripcion}: -{d.modificador} | ";
                                    }
                                }
                                this.contenedor(texto);
                            }
                            List<Extra> resis = new Modelo().listarResistencia(en.idCriatura);
                            if (resis.Count > 0)
                            {
                                string texto = "Resistencias: ";
                                foreach (var d in resis)
                                {
                                    if (d.cantidadR == 0)
                                    {
                                        texto += $"| {d.descripcion}: Inmune | ";
                                    }
                                    else if (d.cantidadR == 0.5)
                                    {
                                        texto += $"| {d.descripcion}: Resistente | ";
                                    }
                                    else
                                    {
                                        texto += $"| {d.descripcion}: Vulnerable | ";
                                    }
                                }
                                this.contenedor(texto);
                            }
                            List<Extra> cond = new Modelo().listarCondicion(en.idCriatura);
                            if (cond.Count > 0)
                            {
                                string texto = "Condiciones: ";
                                foreach (var d in cond)
                                {
                                    texto += $"| {d.descripcion}: Inmune | ";
                                }
                                this.contenedor(texto);
                            }
                            List<Extra> sentidos = new Modelo().listarSentido(en.idCriatura);
                            if (sentidos.Count > 0)
                            {
                                string texto = "Sentidos: ";
                                foreach (var d in sentidos)
                                {
                                    if (d.cantidad > 0)
                                    {
                                        texto += $"| {d.descripcion}: {d.cantidad} pies | ";
                                    }
                                }
                                this.contenedor(texto);
                            }
                            this.VidaActual.Text = $"Vida Actual: {en.vida}";
                            string query = $"SELECT * FROM CRIATURASTATS WHERE IDCRIATURA = {en.idCriatura};";
                            var result = new Modelo().realizarQueryCriaturaStats(query);
                            foreach (var cs in result)
                            {
                                this.CA.Text = $"Clase Armadura: {cs.claseArmadura}";
                                this.Velocidad.Text = $"Velocidad: {cs.velocidad}";
                                this.STR.Text = cs.fuerza.ToString();
                                this.DEX.Text = cs.destreza.ToString();
                                this.CON.Text = cs.constitucion.ToString();
                                this.INT.Text = cs.inteligencia.ToString();
                                this.WIS.Text = cs.sabiduria.ToString();
                                this.CHA.Text = cs.carisma.ToString();
                                this.STR_MOD.Text = Convert.ToString(calcularModificador(cs.fuerza));
                                this.DEX_MOD.Text = Convert.ToString(calcularModificador(cs.destreza));
                                this.CON_MOD.Text = Convert.ToString(calcularModificador(cs.constitucion));
                                this.INT_MOD.Text = Convert.ToString(calcularModificador(cs.inteligencia));
                                this.WIS_MOD.Text = Convert.ToString(calcularModificador(cs.sabiduria));
                                this.CHA_MOD.Text = Convert.ToString(calcularModificador(cs.carisma));
                            }
                            this.enTipo = en.idCriatura;
                            break;
                        }
                    }
                    this.DatosCriatura.Visible = true;
                    this.Nombre.Text = nombre;
                }
                else
                {
                    this.DatosCriatura.Visible = false;
                }
            }
        }

        private void Finalizar_Click(object sender, EventArgs e)
        {
            Form1? parentForm = this.Owner as Form1;
            string query = "DELETE FROM INICIATIVA;";
            string turno1 = "UPDATE TURNO SET NUMTURNO = 1";
            DialogResult result = MessageBox.Show($"¿Quieres finalizar la batalla?", "¿Estás seguro?", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                parentForm.limpiarLista();
                new Modelo().realizarCRUD(query);
                new Modelo().realizarCRUD(turno1);
                MessageBox.Show("Batalla finalizada.");
                this.Close();
            }

        }

        private void HabAcci_Click(object sender, EventArgs e)
        {
            DatosCriatura dc = new DatosCriatura();
            dc.traerDatos(this.enTipo);
            dc.Show();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Container_Paint(object sender, PaintEventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }

}
