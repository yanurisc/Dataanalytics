USE northwind;
/* 1. Create a single query to list the product id, product name, unit price and category
name of all products. Order by category name and within that, by product name.*/
select p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
from products p
Join categories c ON p.CategoryID = c.CategoryID
order by c.CategoryName asc, p.ProductName asc;

/*2. Create a single query to list the product id, product name, unit price and supplier
name of all products that cost more than $75. Order by product name.*/
select p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName
from products p 
join suppliers s on p.SupplierID = s.SupplierID
where p.UnitPrice > 75
order by p.ProductName asc;


/*3. Create a single query to list the product id, product name, unit price, category name,
and supplier name of every product. Order by product name.*/
select p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName, s.CompanyName
from products p
join categories c on P.CategoryID = c.CategoryID
join suppliers s on p.SupplierID = s.SupplierID
order by p.ProductName asc;

/*4. Create a single query to list the order id, ship name, ship address, and shipping
company name of every order that shipped to Germany. Assign the shipping company
name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
shipped to.*/
select o.OrderID, o.ShipName, o.ShipAddress, s.CompanyName as shipper
from orders o 
join shippers s on o.ShipVia = s.ShipperID
where o.ShipCountry = 'Germany' 
order by s.CompanyName asc, o.Shipname asc;

/*5. Start from the same query as above (#4), but omit OrderID and add logic to group by
ship name, with a count of how many orders were shipped for that ship name.*/
select o.ShipName, o.ShipAddress, s.CompanyName as shipper, count(*) as OrderCount
from orders o
join shippers s on o.ShipVia = s.ShipperID
where o.ShipCountry = 'Germany' 
group by o.ShipName, o.ShipAddress, s.CompanyName
order by s.CompanyName asc, o.ShipName asc;

/*6. Create a single query to list the order id, order date, ship name, ship address of all
orders that included Sasquatch Ale.*/
select o.orderID, o.OrderDate, o.ShipName, o.ShipAddress
from orders o
join `order details` od on o.OrderID = od.OrderID
join products p on od.ProductID = p.ProductID
Where p.ProductName = 'Sasquatch Ale'
order by o.OrderID asc;