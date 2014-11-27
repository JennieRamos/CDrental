import unittest
from cd import CD
from cd import Customer
from cd import Check_out
from cd_files import CD_files
from cd_files import Customer_files


class TestCD(unittest.TestCase):
  def test_cd_identity_created(self):
    cd = CD()
    self.assertEqual({}, cd.cd_list) 
    self.assertEqual(len(cd.cd_list), 0)

  def test_customer_identity_created(self):
    customer = Customer()
    self.assertEqual({}, customer.customer) 
    self.assertEqual(len(customer.customer), 0)


  def test_add_cd(self):
    cd = CD()
    cd_1 = CD_files("1" , "cd1")
    cd_2 = CD_files("2", "cd2")
    cd.add_cd(cd_1)
    cd.add_cd(cd_2)
    self.assertEqual(len(cd.cd_list), 2)

  def test_add_customer(self):
    customer = Customer()
    customer_1 = Customer_files("001", "jen")
    customer_2 = Customer_files("002","nicole")
    customer.add_customer(customer_1)
    customer.add_customer(customer_2)
    self.assertEqual(len(customer.customer), 2)

  def test_get_cd(self):
    cd =CD()
    cd_1 = CD_files("1", "cd")
    cd.add_cd(cd_1)
    self.assertEqual(cd.get_cd("1"), "cd")

  def test_get_customer(self):
    customer = Customer()
    customer_1 = Customer_files("001", "jen")
    customer.add_customer(customer_1)
    self.assertEqual(customer.get_customer("001"),"jen")

  def test_check_out_cd_is_iniatially_empty(self):
    check_out = Check_out()
    self.assertEqual({}, check_out.cd_check_out)
    self.assertEqual(len(check_out.cd_check_out), 0)

  
  
  
if __name__ == '__main__':
  unittest.main()
