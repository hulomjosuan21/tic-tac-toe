import streamlit as st

st.set_page_config("JDBC Step by step process by Josuan",layout='centered',initial_sidebar_state='auto',page_icon=":face_in_clouds:")

dataList = ["""public class AppDatabase{
    private String url = "jdbc:mysql://localhost:3306/yourTable";
    private String username = "Your MySQL username"; //example: root
    private String password = "Your MySQL Password"; //example: password123
    
    AppDatabase(){
        try{
            this.connection = DriverManager.getConnection(url, username, password);
            this.statement = connection.createStatement();
        }catch(SQLException e){
            e.printStackTrace();
        }
    }
}   ""","""import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.PreparedStatement;""",
"""SELECT * FROM yourTableName""","""
    public DefaultTableModel getAllRecord(){
        String query = "SELECT * FROM "+tableName;
        DefaultTableModel model = new DefaultTableModel();
        model.setColumnIdentifiers(new Object[]{"Id", "First Name", "Last Name", "Address", "Age"});
        
        try{
            ResultSet result = statement.executeQuery(query);
            
            while(result.next()){
                int id = result.getInt("id");
                String firstName = result.getString("FirstName");
                String lastName = result.getString("LastName");
                String address = result.getString("Address");
                int age = result.getInt("Age");
                System.out.printf("ID: %d\\nFirst name: %s\\nLast name: %s\\nAddress: %s\\nAge: %d",id,firstName,lastName,
                address,age);
                model.addRow(new Object[]{id, firstName, lastName, address, age});
            }
            
            result.close();
        }catch(SQLException e){
            e.printStackTrace();
        }
        return model;
    }
""","import javax.swing.table.DefaultTableModel;","""
    public int addRecord(String f_name, String l_name, String address, int age){
        int returnVal = 0;
        String query = "INSERT INTO tableName+ (id, FirstName, LastName, Address, Age) VALUES (?, ?, ?, ?)";  
        try{
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(1, f_name);
            preparedStatement.setString(2, l_name);
            preparedStatement.setString(3, address);
            preparedStatement.setInt(4, age);
            
            returnVal = preparedStatement.executeUpdate();
            
            preparedStatement.close();
        }catch(SQLException e){
            e.printStackTrace();
        }
        return returnVal;
    }""","""    public int deleteAllRecord(){
        int returnVal = 0;
        String query = "DELETE FROM "+tableName;
        try{

            int rowCount = statement.executeUpdate(query);

            System.out.println("Deleted " + rowCount + " rows from the table.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
        
        return returnVal;
    }   """]

def main():
    st.balloons()
    
    st.title("Java Database Connect (JDBC)")
    st.subheader("Step by step process by Josuan")
    st.write("---")
    
    st.header("IDE used")
    st.image("ide.png")
    st.text("Assuming that you already know the syntax of Java, to create a project and some MySQL queries")
    st.write("---")
    
    st.header("Add MySQL Java Connector .jar file")
    st.subheader("Step #1")
    st.image("Slide1.PNG")
    st.subheader("Step #2")
    st.image("Slide2.PNG")
    st.write("---")    
    
    st.header("Import Libraries")
    st.code(dataList[1])
    st.write("---")    
    
    st.header("Declare Class")
    st.code(dataList[0])
    st.write("---")

    st.header("Example MySQL Query")
    st.code(dataList[2])
    st.write("---")
    
    st.header("Optional Import")
    st.code(dataList[4])
    st.text("You can use this return type so that you can return it and display to Java jTable")
    st.write("---")
    
    st.header("Example Method to Display All Records")
    st.code(dataList[3])
    st.text("You can use also void type method")
    st.write("---")
    
    st.header("Example Method to Insert a Record")
    st.code(dataList[5])
    st.text("int method because this will return 1 or 0 zero means error")
    st.write("---")
    
    st.header("Example Method to Delete All Records")
    st.code(dataList[6])
    st.text("int method because this will return 1 or 0 zero means error")
    st.write("---")
    st.text("If any of this doesn't work, please email me at noahboat231@gmail.com")
    
if __name__ == '__main__':
    main()
