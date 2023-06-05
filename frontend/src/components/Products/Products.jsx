import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Box,
  Checkbox,
  Container,
  FormControlLabel,
  FormGroup,
  Grid,
  Typography,
 } from "@mui/material";
 import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";
 import { useEffect, useState } from "react";
 import Stack from "@mui/material/Stack";
 import LinearProgress from "@mui/material/LinearProgress";
 
 
 const Products = () => {
  const baseUrl = `https://qsl-solutions.onrender.com/`;
 
 
  const [loading, setLoading] = useState(false);
  // const [products, setProduct] = useState([]);
  const [filterData, setFilterData] = useState([]);
 
 
  const [categoryList, setCategoryList] = useState([]);
  const [brandList, setBrandList] = useState([]);
  const [warrentyList, setWarrentyList] = useState([]);
  const [sellerList, setSellerList] = useState([]);
  const [productType, setProductType] = useState([]);
 
 
  const [productTypeFilter, setProductTypeFilter] = useState([]);
  const [productBrand, setProductBrand] = useState([]);
  const [productCatgory, setProductCategory] = useState([]);
  const [productWarrentey, setProductWarrenty] = useState([]);
  const [productSeller, setProductSeller] = useState([]);
  const [minPrice, setMinPrice] = useState("");
  const [maxPrice, setMaxPrice] = useState("");
 
 
  console.log(minPrice, maxPrice);
 
 
  // const [filter, setfilter]=useState("")
 
 
  // product list data fetch
  useEffect(() => {
    const options = { method: "GET" };
    fetch(
      "https://qsl-solutions.onrender.com/api/product/filter/list/",
      options
    )
      .then((response) => response.json())
      .then((data) => {
        setCategoryList(data?.catagory_list);
        setProductType(data?.product_type_list);
        setBrandList(data?.brand_list);
        setWarrentyList(data?.warrenty_list);
        setSellerList(data?.seller_list);
        setLoading(true);
      })
      .catch((err) => console.error(err));
  }, []);
 
 
  // product data fetch
  useEffect(() => {
    const options = { method: "GET" };
    fetch("https://qsl-solutions.onrender.com/api/product/list/", options)
      .then((response) => response.json())
      .then((data) => {
        // setProduct(data?.results);
        setFilterData(data?.results);
      })
      .catch((err) => console.error(err));
  }, []);
 
 
  // const handlePrice = () => {};
 
 
  const handleProductTypeFilter = (item) => {
    if (productTypeFilter.includes(item)) {
      setProductTypeFilter(
        productTypeFilter.filter((selected) => selected !== item)
      );
    } else {
      setProductTypeFilter([...productTypeFilter, item]);
    }
  };
 
 
  const handleProductBand = (item) => {
    if (productBrand.includes(item)) {
      setProductBrand(productBrand.filter((selected) => selected !== item));
    } else {
      setProductBrand([...productBrand, item]);
    }
  };
 
 
  const ProductCategory = (item) => {
    if (productCatgory.includes(item)) {
      setProductCategory(
        productCatgory.filter((selected) => selected !== item)
      );
    } else {
      setProductCategory([...productCatgory, item]);
    }
  };
 
 
  const handleProductWarrenty = (item) => {
    if (productWarrentey.includes(item)) {
      setProductWarrenty(
        productWarrentey.filter((selected) => selected !== item)
      );
    } else {
      setProductWarrenty([...productWarrentey, item]);
    }
  };
 
 
  const handleProductsell = (item) => {
    if (productSeller.includes(item)) {
      setProductSeller(productSeller.filter((selected) => selected !== item));
    } else {
      setProductSeller([...productSeller, item]);
    }
  };
 
 
  // const url = `https://qsl-solutions.onrender.com/api/product/list/?catagory=${productCatgory}&sell_price_min=${minPrice}&brand=${productBrand}&sell_price_max=${maxPrice}&product_type=${productTypeFilter}&warrenty=${productWarrentey}&seller=${productSeller}`;
 
 
  useEffect(() => {
    const options = { method: "GET" };
    const url = `https://qsl-solutions.onrender.com/api/product/list/?&brand=${productBrand}&catagory=${productCatgory}&product_type=${productTypeFilter}&seller=${productSeller}&warrenty=${productWarrentey}&sell_price_min=${minPrice}&sell_price_max=${maxPrice}`;
    console.log(url);
    fetch(url, options)
      .then((response) => response.json())
      .then((data) => {
        setFilterData(data?.results);
      })
      .catch((err) => console.error(err));
  }, [
    productBrand,
    productCatgory,
    productSeller,
    productWarrentey,
    productTypeFilter,
    minPrice,
    maxPrice,
  ]);
  return (
    <Box style={{ background: "#fff", height: "100vh" }}>
      <Box>
        <Container>
          <Box>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={4} md={2.5}>
                <Box
                  className="filter-side-0"
                  boxShado="0px 0px 15px rgba(42, 110, 152, 0.23)"
                  bgcolor="#fff"
                  p={1}
                  borderRadius="5px"
                >
                  <Box>
                    <input
                      type="number"
                      placeholder="Min Price"
                      style={{
                        width: "35%",
                        marginRight: "5px",
                        border: "1px solid #ccc",
                        outline: "none",
                      }}
                      onChange={(e) => setMinPrice(e.target.value)}
                    />
                    <input
                      type="number"
                      placeholder="Max Price"
                      style={{
                        width: "35%",
                        border: "1px solid #ccc",
                        outline: "none",
                        marginRight: "5px",
                      }}
                      onChange={(e) => setMaxPrice(e.target.value)}
                    />
 
 
                    {/* <button
                      style={{
                        background: "#BC6277",
                        width: "50px",
                        color: "#fff",
                        border: "none",
                        cursor: "pointer",
                      }}
                      onClick={() => handlePrice()}
                    >
                      {" "}
                      Go
                    </button> */}
                  </Box>{" "}
                  <Accordion
                    defaultExpanded={true}
                    style={{ margin: "0", boxShadow: "none" }}
                  >
                    <AccordionSummary
                      style={{ margin: "0", padding: "0px" }}
                      expandIcon={<KeyboardArrowUpIcon color="#BC6277" />}
                      id="panel2a-header"
                    >
                      <Typography
                        sx={{
                          color: "#BC6277",
                          fontWeight: 500,
                          fontSize: 13,
                        }}
                      >
                        Product Type
                      </Typography>
                    </AccordionSummary>
                    <AccordionDetails style={{ margin: "0", padding: "0" }}>
                      <Box>
                        <FormGroup>
                          {productType?.map((productType, index) => (
                            <FormControlLabel
                              key={index}
                              checked={productTypeFilter.includes(
                                productType?.name
                              )}
                              onChange={() =>
                                handleProductTypeFilter(productType?.name)
                              }
                              control={<Checkbox className="box-0" />}
                              label={
                                <Typography
                                  sx={{
                                    color: "#BC6277",
                                    fontWeight: 500,
                                    fontSize: 13,
                                  }}
                                >
                                  {productType?.name}
                                </Typography>
                              }
                            />
                          ))}
                        </FormGroup>
                      </Box>
                    </AccordionDetails>
                  </Accordion>
                  <Accordion
                    defaultExpanded={false}
                    style={{ margin: "0", boxShadow: "none" }}
                  >
                    <AccordionSummary
                      style={{ margin: "0", padding: "0px" }}
                      expandIcon={<KeyboardArrowUpIcon color="#BC6277" />}
                      id="panel2a-header"
                    >
                      <Typography
                        sx={{
                          color: "#BC6277",
                          fontWeight: 500,
                          fontSize: 13,
                        }}
                      >
                        Brand List
                      </Typography>
                    </AccordionSummary>
                    <AccordionDetails style={{ margin: "0", padding: "0" }}>
                      <Box>
                        <FormGroup>
                          {brandList?.map((brandList, index) => (
                            <FormControlLabel
                              key={index}
                              checked={productBrand.includes(brandList?.name)}
                              onChange={() =>
                                handleProductBand(brandList?.name)
                              }
                              control={<Checkbox className="box-0" />}
                              label={
                                <Typography
                                  sx={{
                                    color: "#BC6277",
                                    fontWeight: 500,
                                    fontSize: 13,
                                  }}
                                >
                                  {brandList?.name}
                                </Typography>
                              }
                            />
                          ))}
                        </FormGroup>
                      </Box>
                    </AccordionDetails>
                  </Accordion>
                  <Accordion
                    defaultExpanded={false}
                    style={{ margin: "0", boxShadow: "none" }}
                  >
                    <AccordionSummary
                      style={{ margin: "0", padding: "0px" }}
                      expandIcon={<KeyboardArrowUpIcon color="#BC6277" />}
                      id="panel2a-header"
                    >
                      <Typography
                        sx={{
                          color: "#BC6277",
                          fontWeight: 500,
                          fontSize: 13,
                        }}
                      >
                        Catagory list
                      </Typography>
                    </AccordionSummary>
                    <AccordionDetails style={{ margin: "0", padding: "0" }}>
                      <Box>
                        <FormGroup>
                          {categoryList?.map((categoryList, index) => (
                            <FormControlLabel
                              key={index}
                              control={<Checkbox className="box-0" />}
                              checked={productCatgory.includes(
                                categoryList?.name
                              )}
                              onChange={() =>
                                ProductCategory(categoryList?.name)
                              }
                              label={
                                <Typography
                                  sx={{
                                    color: "#BC6277",
                                    fontWeight: 500,
                                    fontSize: 13,
                                  }}
                                >
                                  {categoryList?.name}
                                </Typography>
                              }
                            />
                          ))}
                        </FormGroup>
                      </Box>
                    </AccordionDetails>
                  </Accordion>
                  <Accordion
                    defaultExpanded={false}
                    style={{ margin: "0", boxShadow: "none" }}
                  >
                    <AccordionSummary
                      style={{ margin: "0", padding: "0px" }}
                      expandIcon={<KeyboardArrowUpIcon color="#BC6277" />}
                      id="panel2a-header"
                    >
                      <Typography
                        sx={{
                          color: "#BC6277",
                          fontWeight: 500,
                          fontSize: 13,
                        }}
                      >
                        Warrenty List
                      </Typography>
                    </AccordionSummary>
                    <AccordionDetails style={{ margin: "0", padding: "0" }}>
                      <Box>
                        <FormGroup>
                          {warrentyList?.map((warrentyList, index) => (
                            <FormControlLabel
                              key={index}
                              checked={productWarrentey.includes(
                                warrentyList?.name
                              )}
                              onChange={() =>
                                handleProductWarrenty(warrentyList?.name)
                              }
                              control={<Checkbox className="box-0" />}
                              label={
                                <Typography
                                  sx={{
                                    color: "#BC6277",
                                    fontWeight: 500,
                                    fontSize: 13,
                                  }}
                                >
                                  {warrentyList?.name}
                                </Typography>
                              }
                            />
                          ))}
                        </FormGroup>
                      </Box>
                    </AccordionDetails>
                  </Accordion>
                  <Accordion
                    defaultExpanded={false}
                    style={{ margin: "0", boxShadow: "none" }}
                  >
                    <AccordionSummary
                      style={{ margin: "0", padding: "0px" }}
                      expandIcon={<KeyboardArrowUpIcon color="#BC6277" />}
                      id="panel2a-header"
                    >
                      <Typography
                        sx={{
                          color: "#BC6277",
                          fontWeight: 500,
                          fontSize: 13,
                        }}
                      >
                        Seller List
                      </Typography>
                    </AccordionSummary>
                    <AccordionDetails style={{ margin: "0", padding: "0" }}>
                      <Box>
                        <FormGroup>
                          {sellerList?.map((sellerList, index) => (
                            <FormControlLabel
                              key={index}
                              checked={productSeller.includes(sellerList?.name)}
                              onChange={() =>
                                handleProductsell(sellerList?.name)
                              }
                              control={<Checkbox className="box-0" />}
                              label={
                                <Typography
                                  sx={{
                                    color: "#BC6277",
                                    fontWeight: 500,
                                    fontSize: 13,
                                  }}
                                >
                                  {sellerList?.name}
                                </Typography>
                              }
                            />
                          ))}
                        </FormGroup>
                      </Box>
                    </AccordionDetails>
                  </Accordion>
                </Box>
              </Grid>
 
 
              <Grid item xs={12} sm={8} md={9.5}>
                {loading ? (
                  <Grid container>
                    {filterData?.map((product, index) => (
                      <Grid key={index} item xs={12} sm={6} md={4}>
                        <Box
                          sx={{
                            backgroundColor: "#ccc",
                            padding: "15px",
                            m: 0.5,
                          }}
                        >
                          <Box>
                            <img
                              src={`${baseUrl}${product?.image}`}
                              alt="productImg"
                              style={{ width: "100%", height: "200px" }}
                            />
                          </Box>
                          <Box style={{ textAlign: "center" }} my={1}>
                            <Typography>Name:{product?.name}</Typography>
                          </Box>
                          <Typography>{product?.brand}</Typography>
                          <Box style={{ textAlign: "center" }} mb={2}>
                            <Typography>
                              Price:{product?.discounted_sell_price}
                            </Typography>
                            <del>Price:{product?.normal_sell_price}</del>
                          </Box>
 
 
                          <Box
                            style={{
                              display: "flex",
                              justifyContent: "space-between",
                            }}
                          >
                            <button
                              style={{
                                width: "80px",
                                height: "30px",
                                cursor: "pointer",
                                background: "#702C8B",
                                border: "none",
                                color: "#fff",
                                borderRadius: "5px",
                              }}
                            >
                              Book{" "}
                            </button>
                            <button
                              style={{
                                width: "80px",
                                height: "30px",
                                cursor: "pointer",
                                background: "#BC6277",
                                border: "none",
                                color: "#fff",
                                borderRadius: "5px",
                              }}
                            >
                              wishList
                            </button>
                          </Box>
                        </Box>
                      </Grid>
                    ))}
                  </Grid>
                ) : (
                  <Stack
                    sx={{ width: "100%", color: "grey.500" }}
                    spacing={2}
                    mt={8}
                  >
                    <LinearProgress color="secondary" />
                    <LinearProgress color="success" />
                    <LinearProgress color="inherit" />
                  </Stack>
                )}
              </Grid>
            </Grid>
          </Box>
        </Container>
      </Box>
    </Box>
  );
 };
 
 
 export default Products;
 
 
 
 





